import re

PHONE_PATTERN = re.compile(r'^(\+?1[-.\s]?)?(\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}$')

def validate_phone(phone_number):
    if not isinstance(phone_number, str):
        return False
    if not PHONE_PATTERN.match(phone_number):
        return False
    digits_only = re.sub(r'[^\d]', '', phone_number)
    if len(digits_only) == 10:
        return True
    if len(digits_only) == 11 and digits_only[0] == '1':
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        "1234567890",
        "123-456-7890",
        "(123) 456-7890",
        "123.456.7890",
        "123 456 7890",
        "+1 123-456-7890",
        "+1 (123) 456-7890",
        "11234567890",
        "123456789",
        "123-456-789",
        "abc-def-ghij",
        "",
        "123-456-78901",
        "(123)456-7890",
        "1 (123) 456-7890"
    ]
    for case in test_cases:
        print(validate_phone(case))