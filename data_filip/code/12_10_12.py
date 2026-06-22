import re

def validate_phone(phone_number):
    pattern = re.compile(r'^(\+?1[-.\s]?)?(\(?[2-9]\d{2}\)?[-.\s]?)?[2-9]\d{2}[-.\s]?\d{4}$')
    return bool(pattern.match(phone_number))

if __name__ == '__main__':
    test_cases = [
        "123-456-7890",
        "(123) 456-7890",
        "1234567890",
        "+1 123 456 7890",
        "123.456.7890",
        "123-456-789",
        "000-123-4567",
        "123-123-4567",
        "abc-def-ghij",
        "12345",
        "(123)456-7890",
        "+1(123)456-7890"
    ]
    for case in test_cases:
        print(validate_phone(case))