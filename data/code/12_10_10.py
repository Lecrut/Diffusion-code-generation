import re

PHONE_PATTERN = re.compile(r'^\(?[0-9]{3}\)?[-.]?[0-9]{3}[-.]?[0-9]{4}$')

def validate_phone(phone_number):
    return bool(PHONE_PATTERN.match(phone_number))

if __name__ == '__main__':
    test_cases = [
        "5551234567",
        "555-123-4567",
        "(555)123-4567",
        "(555) 123-4567",
        "123456789",
        "555-12-4567",
        "(55)123-4567",
        "555.123.4567"
    ]
    for number in test_cases:
        print(validate_phone(number))