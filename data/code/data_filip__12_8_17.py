import re

def validate_mobile(number):
    return bool(re.fullmatch(r'^\+?[1-9]\d{9,14}$', number))

if __name__ == '__main__':
    sample_number = "+1234567890"
    print(validate_mobile(sample_number))