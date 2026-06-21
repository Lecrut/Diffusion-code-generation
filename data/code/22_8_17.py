import string
import re

COMMON_WORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "master", "dragon", "111111", "baseball",
    "iloveyou", "trustno1", "sunshine", "princess", "football",
    "charlie", "shadow", "michael", "jessica", "pepper"
]

def validate_password_strength(password: str) -> dict:
    results = {
        "valid": True,
        "errors": []
    }

    if len(password) < 8:
        results["valid"] = False
        results["errors"].append("Password must be at least 8 characters long.")

    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not (has_upper and has_lower and has_digit and has_special):
        results["valid"] = False
        results["errors"].append("Password must contain uppercase, lowercase, digit, and special character.")

    if password.lower() in COMMON_WORDS:
        results["valid"] = False
        results["errors"].append("Password is too common.")

    common_word_found = False
    lower_password = password.lower()
    for word in COMMON_WORDS:
        if word != "111111" and word in lower_password and len(word) >= 4:
            common_word_found = True
            break
    
    if common_word_found:
        results["valid"] = False
        results["errors"].append("Password contains a common dictionary word.")

    if re.search(r"(.)\1{2,}", password):
        results["valid"] = False
        results["errors"].append("Password contains sequences of 3 or more identical characters.")

    if re.search(r"(012|123|234|345|456|567|678|789|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)", lower_password):
        results["valid"] = False
        results["errors"].append("Password contains sequential characters.")

    return results

if __name__ == '__main__':
    test_passwords = [
        "Str0ng!Pass",
        "weak",
        "password123",
        "Alluppercasenodigit!",
        "Nodigit!WithWord",
        "111111aaaa"
    ]

    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(f"Password: '{pwd}' -> Valid: {result['valid']}, Errors: {result['errors']}")