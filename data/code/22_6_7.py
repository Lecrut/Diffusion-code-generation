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
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2] == password[i+3] if i+3 < len(password) else False:
            return False
    if len(password) >= 4:
        for i in range(len(password) - 3):
            if password[i] == password[i+1] == password[i+2] == password[i+3]:
                return False
    return True

if __name__ == '__main__':
    test_passwords = [
        "Password1!",
        "pass",
        "PASSWORD1!",
        "Password123",
        "Pass1234",
        "Passw0rd!1",
        "aaaa1234!",
        "Aa1!bbbbbb",
        "Valid1!P@ss"
    ]
    for pw in test_passwords:
        print(validate_password_strength(pw))