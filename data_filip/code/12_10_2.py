import re

PHONE_PATTERN = re.compile(r'^\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}$')

def validate_phone(phone_number):
    return bool(PHONE_PATTERN.match(phone_number))

if __name__ == '__main__':
    test_cases = [
        "1234567890",
        "123-456-7890",
        "(123) 456-7890",
        "(123)456-7890",
        "123 456 7890",
        "12-345-67890",
        "12345678901",
        "abc-def-ghij"
    ]

    for case in test_cases:
        print(validate_phone(case))