import re

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
        return False
    return True

if __name__ == '__main__':
    print(validate_password("Short1!"))
    print(validate_password("LongEnough"))
    print(validate_password("NoSpecial1"))
    print(validate_password("noUppercase1!"))
    print(validate_password("ValidPass1!"))
    print(validate_password("12345678"))
    print(validate_password("ABCDEFGH"))
    print(validate_password("!@#$%^&*"))
    print(validate_password("Valid1!Pass"))