import re

def validate_password_strength(password):
    if not password:
        return False
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    if re.search(r'(.)\1{3,}', password):
        return False
    return True

if __name__ == '__main__':
    test_passwords = [
        "Abc123!abc",
        "Aa1!aaaa",
        "Short1!",
        "NoSpecial123",
        "AllLower1!",
        "AllUpper1!",
        "NoDigits!",
        "ValidPass1!",
        "aaaaB1!",
        "Abc123!a"
    ]
    for pwd in test_passwords:
        print(validate_password_strength(pwd))