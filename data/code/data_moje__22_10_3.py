def validate_password_strength(password):
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    return has_upper and has_lower and has_digit and has_special

if __name__ == '__main__':
    test_cases = [
        "WeakPass",
        "StrongP@ss1",
        "short1!",
        "Alllowercase1!",
        "ALLUPPERCASE1!",
        "12345678",
        "ValidP@ss2023",
        ""
    ]
    for case in test_cases:
        result = validate_password_strength(case)
        print(f"Password: '{case}' -> {result}")