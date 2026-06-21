import re

def validate_mobile_number(phone_number: str) -> bool:
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    print(validate_mobile_number("+1234567890"))
    print(validate_mobile_number("123-456-7890"))
    print(validate_mobile_number("+9876543210"))