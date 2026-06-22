import re

def is_valid_us_phone_number(phone_number):
    if not isinstance(phone_number, str):
        return False
    pattern = re.compile(r'^\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$')
    return bool(pattern.match(phone_number))

if __name__ == '__main__':
    test_cases = [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "1234567890",
        "123 456 7890",
        "12-345-6789",
        "1234-567-890",
        "abc-def-ghij"
    ]
    for number in test_cases:
        result = is_valid_us_phone_number(number)
        print(f"{number}: {result}")