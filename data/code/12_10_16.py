import re

_phone_pattern = re.compile(r'^(\d{3}|\(\d{3}\))[-.]?\d{3}[-.]?\d{4}$')

def validate_phone(number):
    return bool(_phone_pattern.match(number))

if __name__ == '__main__':
    test_cases = [
        "1234567890",
        "123-456-7890",
        "(123)456-7890",
        "(123) 456-7890",
        "123.456.7890",
        "123456789",
        "12345678901",
        "abc-def-ghij"
    ]
    for case in test_cases:
        print(validate_phone(case))