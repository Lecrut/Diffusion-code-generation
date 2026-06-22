import re

PHONE_PATTERN = re.compile(r'^(\d{3}|\(\d{3}\))[\s-]?\d{3}[\s-]?\d{4}$')

def validate_phone(phone_number):
    if not isinstance(phone_number, str):
        return False
    return bool(PHONE_PATTERN.match(phone_number))

if __name__ == '__main__':
    test_cases = [
        "1234567890",
        "123-456-7890",
        "(123)456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "123456789",
        "12345678901",
        "12-34-56-78",
        "abc-def-ghij"
    ]
    
    for case in test_cases:
        result = validate_phone(case)
        print(f"{case}: {result}")