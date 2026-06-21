import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

if __name__ == '__main__':
    test_passwords = ["Short1!", "ValidPass1!", "nospaces1", "ALLCAPS1!", "lowercase1!", "Valid@Pass"]
    for pwd in test_passwords:
        result = is_valid_password(pwd)
        print(pwd, result)