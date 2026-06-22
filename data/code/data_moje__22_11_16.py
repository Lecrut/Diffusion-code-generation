import re

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'
    return bool(re.match(pattern, password))

if __name__ == '__main__':
    samples = [
        "Short1!",
        "NoDigits!",
        "NoUppercase1!",
        "NoSpecial1A",
        "Valid1A!",
        "Complexity!9z",
        "12345678",
        "Aa!b2cD3",
    ]
    for sample in samples:
        print(validate_password(sample))