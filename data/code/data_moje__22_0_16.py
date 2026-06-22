import re

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

if __name__ == '__main__':
    print(validate_password("Short1!"))
    print(validate_password("NoSpecial1a"))
    print(validate_password("NoDigit!aA"))
    print(validate_password("NoUpper!1a"))
    print(validate_password("NoLower!1A"))
    print(validate_password("Valid1!aA"))