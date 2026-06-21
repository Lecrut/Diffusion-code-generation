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
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', password):
        return False
    return True

if __name__ == '__main__':
    test_passwords = [
        "short1A!",
        "nouppercase1!",
        "nolowercase1!",
        "nodigitA!b",
        "nospecialAb1",
        "ValidPass1!",
        "AnotherStrong1@",
        "12345678",
        "ABCDEFGH",
        "abcdefgh",
        "Aa1!",
    ]
    for pwd in test_passwords:
        result = validate_password(pwd)
        print(result)