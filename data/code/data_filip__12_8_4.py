import re

validate_mobile = lambda s: bool(re.fullmatch(r'^\+?1?\d{9,15}$', s))

if __name__ == '__main__':
    phone = "+1234567890"
    print(validate_mobile(phone))