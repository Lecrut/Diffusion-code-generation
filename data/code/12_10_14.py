import re

PHONE_PATTERN = re.compile(r'^(\d{3}[-.]?\d{3}[-.]?\d{4}|\(\d{3}\)\s?\d{3}[-.]?\d{4})$')

def validate_phone(phone_number: str) -> bool:
    return bool(PHONE_PATTERN.match(phone_number))

if __name__ == '__main__':
    test_cases = [
        "1234567890",
        "123-456-7890",
        "(123) 456-7890",
        "(123)456-7890",
        "123.456.7890",
        "123-45-6789",
        "abc-def-ghij",
        "12345678901",
        "123 456 7890",
        "+1-123-456-7890"
    ]
    
    for case in test_cases:
        print(validate_phone(case))