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
    if not re.search(r'[^A-Za-z0-9]', password):
        return False
    return True

if __name__ == '__main__':
    passwords = [
        "Short1!",
        "nouppercase1!",
        "NOLOWERCASE1!",
        "NoSpecial1",
        "Nodigits!",
        "ValidPass1!",
        "Weak",
        "AnotherValid2#Password"
    ]
    results = {pw: validate_password_strength(pw) for pw in passwords}
    print(results)