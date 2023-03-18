import re
from unittest.mock import MagicMock

import lucianodlf
from lucianodlf import generateRandomPassword


def test_password_lenght_right():
    assert len(generateRandomPassword(8)) == 8
    assert len(generateRandomPassword(16)) == 16


def test_password_lenght_bad():
    assert generateRandomPassword(7) == None
    assert generateRandomPassword(19) == None


def test_password_with_upper_case_letters():
    lucianodlf.getRandomLowerLetter = MagicMock(return_value=69)
    password = generateRandomPassword(8, True)
    assert 'E' in password


def test_password_with_numbers():
    lucianodlf.getRandomNumber = MagicMock(return_value=57)
    password = generateRandomPassword(8, True, True)
    assert '9' in password

def test_password_with_simbols():
    lucianodlf.getRandomSimbol = MagicMock(return_value=40)
    password = generateRandomPassword(8, True, True, True)
    assert '(' in password

def test_password_with_full_characters():
    password = generateRandomPassword(16, True, True, True)
    print(password)
    with_lower_case_letters = re.search(r'[a-z]', password) 
    with_upper_case_letters = re.search(r'[A-Z]', password)
    with_numbers = re.search(r'\d', password)
    with_simbols = re.search(r'[$-/:-?{-~!"^_`\[\]\(\)]', password)
    assert with_lower_case_letters != None
    assert with_upper_case_letters != None
    assert with_numbers != None
    assert with_simbols != None