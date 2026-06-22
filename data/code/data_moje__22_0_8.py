import re

def validate_password_strength(password: str) -> bool:
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
    print(validate_password_strength("Secure1!"))
    print(validate_password_strength("weak"))
    print(validate_password_strength("NoDigitsHere!"))
    print(validate_password_strength("nouppercase1!"))
    print(validate_password_strength("NOLOWERCASE1!"))
    print(validate_password_strength("NoSpecial1"))
    print(validate_password_strength("Short1!"))