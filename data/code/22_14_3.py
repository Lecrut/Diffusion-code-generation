import string
import re

COMMON_WEAK_PASSWORDS = {
    "123456", "password", "12345678", "qwerty", "abc123",
    "111111", "123456789", "letmein", "welcome", "monkey"
}

def is_sequential(password):
    if len(password) < 3:
        return False
    for i in range(len(password) - 2):
        if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i+1]) + 1:
            return True
        if ord(password[i+1]) == ord(password[i]) - 1 and ord(password[i+2]) == ord(password[i+1]) - 1:
            return True
    return False

def validate_password_strength(password):
    if password in COMMON_WEAK_PASSWORDS:
        return False
    if len(password) < 8:
        return False
    if is_sequential(password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

if __name__ == '__main__':
    test_cases = ["Password1!", "123456", "Abcdefgh1!", "Qwerty123!", "Str0ngP@ss"]
    for case in test_cases:
        result = validate_password_strength(case)
        print(result)