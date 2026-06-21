import re
import string
import unicodedata

COMMON_PASSWORDS = [
    "password", "123456789", "12345678", "123456", "qwerty",
    "abc123", "monkey", "master", "dragon", "111111",
    "baseball", "iloveyou", "trustno1", "sunshine", "princess",
    "football", "shadow", "superman", "michael", "654321",
    "access", "login", "welcome", "hello", "charlie"
]

def validate_password_strength(password: str) -> dict:
    if not isinstance(password, str):
        return {
            "is_valid": False,
            "reason": "Password must be a string"
        }

    errors = []

    if len(password) < 8:
        errors.append("Password is too short (minimum 8 characters)")

    if not any(c.isupper() for c in password):
        errors.append("Missing uppercase letter")

    if not any(c.islower() for c in password):
        errors.append("Missing lowercase letter")

    if not any(c.isdigit() for c in password):
        errors.append("Missing digit")

    if not any(c in string.punctuation for c in password):
        errors.append("Missing special character")

    password_lower = password.lower()
    if password_lower in COMMON_PASSWORDS:
        errors.append("Password contains a common dictionary word")

    if errors:
        return {
            "is_valid": False,
            "errors": errors
        }

    return {
        "is_valid": True,
        "strength": "Strong"
    }

if __name__ == '__main__':
    sample_password = "P@ssw0rd!Str0ng"
    result = validate_password_strength(sample_password)
    print(result)

    sample_weak = "123456"
    result_weak = validate_password_strength(sample_weak)
    print(result_weak)