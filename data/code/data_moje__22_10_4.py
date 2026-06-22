def validate_password_strength(password):
    if not password or len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = set("!@#$%^&*()_+-=[]{}|;:',.<>?/`~")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    return has_upper and has_lower and has_digit and has_special

if __name__ == '__main__':
    sample_passwords = [
        "Short1!",
        "alllowercase1",
        "ALLUPPERCASE1",
        "NoDigitsHere!",
        "Valid1!Pass",
        "Valid1!Passx"
    ]

    for pwd in sample_passwords:
        print(validate_password_strength(pwd))