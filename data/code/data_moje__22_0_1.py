import re

def validate_password_strength(password):
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
    return True

if __name__ == '__main__':
    print(validate_password_strength('StrongP@ss1'))
    print(validate_password_strength('weak'))
    print(validate_password_strength('AllUppercase1!'))
    print(validate_password_strength('alllowercase1!'))
    print(validate_password_strength('NoSpecialChar1'))
    print(validate_password_strength('NoDigits!'))
    print(validate_password_strength('NoUpper!1'))
    print(validate_password_strength('NoLower!1'))