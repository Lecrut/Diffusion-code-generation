import re

def validate_password(password):
    pattern = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$')
    return bool(pattern.match(password))

if __name__ == '__main__':
    test_passwords = [
        "short",
        "NoSpecial1",
        "NoDigit!",
        "nouppercase1!",
        "Valid1!",
        "A1!bcdefg",
        "ALLUPPERCASE1!",
        "alllowercase1!",
        "12345678",
        "ABCDEFGH",
        "!@#$%^&*",
        "ValidPass1!",
    ]
    for pwd in test_passwords:
        print(validate_password(pwd))