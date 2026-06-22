def validate_password_strength(password):
    if not isinstance(password, str) or len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
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
    test_passwords = [
        "Short1!",
        "NoSpecialChar1",
        "NoDigitSpecialChar",
        "NoUpperCase1!",
        "NoLowerCase1!",
        "ValidPassw0rd!",
        "AnotherG00d#Pass"
    ]
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(f"{pwd}: {result}")