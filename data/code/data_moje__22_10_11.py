def validate_password_strength(password):
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = set("!@#$%^&*()_+-=[]{}|;:',.<>?/")
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
        if has_upper and has_lower and has_digit and has_special:
            return True
    return False

if __name__ == '__main__':
    test_passwords = [
        "Secure1!",
        "weak",
        "nouppercase1!",
        "NOLOWERCASE1!",
        "NoDigits!!!!",
        "12345678",
        "Short!a1",
        "Perfect123#Pass"
    ]
    results = [validate_password_strength(pw) for pw in test_passwords]
    print(results)