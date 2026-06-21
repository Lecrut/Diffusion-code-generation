import re

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

if __name__ == '__main__':
    test_passwords = ["Abc12345!", "weak", "NOLOWERCASE123!", "nolowercasewithspecial@123", "ValidPass1!"]
    for p in test_passwords:
        print(f"{p}: {validate_password(p)}")