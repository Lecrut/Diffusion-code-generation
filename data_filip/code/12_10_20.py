import re

PHONE_PATTERN = re.compile(r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$')

def validate_phone(phone_number: str) -> bool:
    if PHONE_PATTERN.match(phone_number):
        return True
    return False

if __name__ == '__main__':
    test_numbers = [
        "1234567890",
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "123456789",
        "123-456-789",
        "123-45-6789",
        "abcdef1234"
    ]

    for number in test_numbers:
        print(validate_phone(number))