import re

validate_mobile = lambda phone: bool(re.fullmatch(r'\+?[1-9]\d{1,14}', phone.strip()))

if __name__ == '__main__':
    print(validate_mobile('+1234567890'))
    print(validate_mobile('1234567890'))
    print(validate_mobile('invalid'))