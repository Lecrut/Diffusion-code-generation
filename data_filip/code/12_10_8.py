import re

PHONE_REGEX = re.compile(r'^(1\s?)?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}$')

def validate_phone(phone_number):
    if not isinstance(phone_number, str):
        return False
    return PHONE_REGEX.match(phone_number) is not None

if __name__ == '__main__':
    test_cases = [
        "1234567890",
        "123-456-7890",
        "(123) 456-7890",
        "1 123 456 7890",
        "11234567890",
        "123-45-6789",
        "abc-def-ghij",
        "",
        "12345678901",
        "(123)456-7890",
        "123456789",
        "1-123-456-7890",
        "123 456 7890"
    ]
    for case in test_cases:
        result = validate_phone(case)
        print(result)