import sys
import os

def check_password_strength(password: str) -> dict:
    if not password:
        return {'strength': 0, 'has_uppercase': False, 'has_lowercase': False, 'has_digit': False, 'has_special': False, 'length': 0, 'score': 0}
    score = 0
    length = len(password)
    score += min(length * 4, 32)
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    flags = 0
    for char in password:
        code = ord(char)
        if 65 <= code <= 90:
            has_uppercase = True
            flags |= 1
        elif 97 <= code <= 122:
            has_lowercase = True
            flags |= 2
        elif 48 <= code <= 57:
            has_digit = True
            flags |= 4
        else:
            has_special = True
            flags |= 8
        if code < 128:
            score += 1
    if flags & 1 and flags & 2:
        score += 8
    if flags & 1 and flags & 4:
        score += 8
    if flags & 1 and flags & 8:
        score += 8
    if flags & 2 and flags & 4:
        score += 8
    if flags & 2 and flags & 8:
        score += 8
    if flags & 4 and flags & 8:
        score += 8
    if flags == 15:
        score += 20
    strength = min(score, 100)
    return {'strength': strength, 'has_uppercase': has_uppercase, 'has_lowercase': has_lowercase, 'has_digit': has_digit, 'has_special': has_special, 'length': length, 'score': score}
if __name__ == '__main__':
    test_password = 'P@ssw0rd!234'
    result = check_password_strength(test_password)
    print(result)