def validate_password_strength(password: str) -> bool:
    if not password or len(password) < 8:
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
        else:
            has_special = True

    return has_upper and has_lower and has_digit and has_special

if __name__ == '__main__':
    sample_passwords = [
        "Abc123!",
        "abc123",
        "ABCDEFGHI",
        "12345678",
        "a1!",
        "Short1!",
        "Valid1234$",
        "AnotherOne#1"
    ]

    for password in sample_passwords:
        result = validate_password_strength(password)
        print(result)