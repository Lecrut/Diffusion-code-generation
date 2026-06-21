import re

def validate_password_strength(password):
    if len(password) < 8:
        return False
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))
    return has_upper and has_lower and has_digit and has_special

if __name__ == '__main__':
    test_cases = [
        "Short",
        "NoSpecialChar1!",
        "NoDigitAbc!",
        "NounpP1!",
        "ValidPass123!",
        "AnotherG0odP@ss",
        "weakpass",
        "WEAKPASSWORD"
    ]
    results = []
    for case in test_cases:
        result = validate_password_strength(case)
        results.append((case, result))
    for item in results:
        print(item)