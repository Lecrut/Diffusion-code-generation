import re

def validate_password_complexity(password):
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,.<>?/\\|[\]`~])[A-Za-z\d!@#$%^&*()\-_=+{};:,.<>?/\\|[\]`~]{8,}$')
    return bool(pattern.match(password))

if __name__ == '__main__':
    sample_passwords = [
        "Pass123!",
        "weak",
        "StrongButNoSpecial1",
        "NoDigitOrUpperSpecial!",
        "ValidP@ss1",
        "12345678",
        "ABCDEFGH",
        "SpecialOnly@#$%"
    ]
    for pwd in sample_passwords:
        print(validate_password_complexity(pwd))