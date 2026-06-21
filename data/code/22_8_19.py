import string
import re

def is_weak_password(password: str) -> bool:
    common_words = [
        "password", "123456", "12345678", "qwerty", "abc123",
        "monkey", "master", "dragon", "111111", "baseball",
        "iloveyou", "trustno1", "sunshine", "princess", "football"
    ]
    for word in common_words:
        if word in password.lower():
            return True
    return False

def validate_password_strength(password: str) -> dict:
    result = {
        "length_ok": len(password) >= 8,
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_special": any(c in string.punctuation for c in password),
        "not_weak": not is_weak_password(password)
    }
    result["overall_valid"] = all(result.values())
    return result

if __name__ == '__main__':
    test_password = "Str0ng!Pass"
    output = validate_password_strength(test_password)
    print(output)