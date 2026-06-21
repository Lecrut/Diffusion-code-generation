import re

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]).{8,}$'
    return bool(re.match(pattern, password))

if __name__ == '__main__':
    print(validate_password('Short1!'))
    print(validate_password('Valid1A!'))
    print(validate_password('NoSpecial1A'))
    print(validate_password('NoUpper1!'))
    print(validate_password('NoDigitA!'))
    print(validate_password('TooShort1!'))
    print(validate_password('PerfectP@ss1'))