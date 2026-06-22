import re
import string

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123",
    "monkey", "master", "dragon", "111111", "baseball",
    "iloveyou", "trustno1", "sunshine", "letmein", "football",
    "shadow", "123123", "654321", "superman", "qazwsx"
}

SEQUENCES = [
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "zyxwvutsrqponmlkjihgfedcba"
]

def _contains_sequential_chars(password, min_length=3):
    lower_pass = password.lower()
    for sequence in SEQUENCES:
        for i in range(len(sequence) - min_length + 1):
            substring = sequence[i:i + min_length]
            if substring in lower_pass:
                return True
    return False

def _has_uppercase(password):
    return any(c.isupper() for c in password)

def _has_lowercase(password):
    return any(c.islower() for c in password)

def _has_digit(password):
    return any(c.isdigit() for c in password)

def _has_special(password):
    return any(c in string.punctuation for c in password)

def validate_password(password):
    if len(password) < 8:
        return {"valid": False, "reason": "Password too short"}
    if password.lower() in COMMON_PASSWORDS:
        return {"valid": False, "reason": "Password is common"}
    if _contains_sequential_chars(password):
        return {"valid": False, "reason": "Password contains sequential characters"}
    if not _has_uppercase(password):
        return {"valid": False, "reason": "Missing uppercase letter"}
    if not _has_lowercase(password):
        return {"valid": False, "reason": "Missing lowercase letter"}
    if not _has_digit(password):
        return {"valid": False, "reason": "Missing digit"}
    if not _has_special(password):
        return {"valid": False, "reason": "Missing special character"}
    return {"valid": True, "reason": "Strong password"}

if __name__ == '__main__':
    test_cases = [
        "Password1!",
        "password123",
        "1234567890abcdef",
        "Complex#Pass99",
        "short1A!",
        "sequential1aB@abc"
    ]
    for pwd in test_cases:
        result = validate_password(pwd)
        print(f"{pwd}: {result['valid']} - {result['reason']}")