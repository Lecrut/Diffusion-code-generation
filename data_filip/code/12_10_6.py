import re

PHONE_PATTERN = re.compile(r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')

def validate_phone(phone: str) -> bool:
    if not isinstance(phone, str):
        return False
    return bool(PHONE_PATTERN.match(phone))

if __name__ == '__main__':
    test_cases = [
        "1234567890",
        "123-456-7890",
        "(123) 456-7890",
        "(123)456-7890",
        "123.456.7890",
        "12-3456-7890",
        "123456789",
        "12345678901",
        "abc-def-ghij"
    ]
    for number in test_cases:
        print(validate_phone(number))