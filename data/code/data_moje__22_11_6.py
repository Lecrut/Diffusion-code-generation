import re

def validate_password_complexity(password):
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[^a-zA-Z0-9]', password):
        return False
    return True

if __name__ == '__main__':
    sample_passwords = [
        "SecurePass1!",
        "short1A!",
        "AllLowercase1!",
        "NoDigitHere!",
        "NoSpecialChar1",
        "NoUppercase1!",
        "ValidPassword123@",
        "Weak1!"
    ]
    for pwd in sample_passwords:
        result = validate_password_complexity(pwd)
        print(result)