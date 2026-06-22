def validate_password_strength(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")
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
        "Alllowercase1!",
        "ALLUPPERCASE1!",
        "NoSpecialChars1",
        "NoDigitsHere!",
        "ValidP@ss1",
        "AnotherValid!12",
        ""
    ]
    for pwd in test_passwords:
        print(validate_password_strength(pwd))