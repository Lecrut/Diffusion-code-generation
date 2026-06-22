import re

phone_pattern = re.compile(r"^(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10})$")

def validate_phone(phone_number):
    return bool(phone_pattern.match(phone_number))

if __name__ == '__main__':
    test_cases = [
        "(123) 456-7890",
        "(123)456-7890",
        "123-456-7890",
        "1234567890",
        "123-456-789",
        "abc-def-ghij",
        "12345",
        "(123) 4567-890",
        "123-456-78901"
    ]
    for case in test_cases:
        print(validate_phone(case))