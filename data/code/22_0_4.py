import re

def validate_password_strength(password):
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
    print(validate_password_strength("Short1!"))
    print(validate_password_strength("NoSpecial1a"))
    print(validate_password_strength("NoDigit!a"))
    print(validate_password_strength("noLower1!"))
    print(validate_password_strength("noUpper1!"))
    print(validate_password_strength("Valid1!a"))
    print(validate_password_strength("ComplexPass123!@#"))