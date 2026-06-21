import re
import string

COMMON_WORDS = {
    "password", "123456", "qwerty", "abc123", "letmein", "welcome", "monkey",
    "dragon", "master", "hello", "trustno1", "sunshine", "princess", "football",
    "iloveyou", "baseball", "access", "shadow", "superman", "batman", "passw0rd",
    "admin", "test", "guest", "charlie", "love", "12345678", "123456789",
    "1234567890", "password1", "password123", "welcome1", "summer", "winter",
    "spring", "autumn", "monkey1", "iloveyou1", "loveyou", "starwars", "super"
}

def validate_password_strength(password):
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    lower_password = password.lower()
    for word in COMMON_WORDS:
        if word in lower_password:
            return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True
    if not (has_upper and has_lower and has_digit and has_special):
        return False
    return True

if __name__ == '__main__':
    test_passwords = [
        "StrongP@ssw0rd!",
        "password123",
        "Short1!",
        "AllUpper@1",
        "NoNumbersHere!",
        "CorrectHorseBatteryStaple!"
    ]
    for pwd in test_passwords:
        print(f"{pwd}: {validate_password_strength(pwd)}")