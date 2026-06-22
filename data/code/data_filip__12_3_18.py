import re

def validate_us_phone(phone_number):
    pattern = r'^(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_numbers = [
        "(123) 456-7890",
        "123-456-7890",
        "1234567890",
        "(123)456-7890",
        "123 456 7890",
        "invalid",
        "123-45-67890",
        "(123) 456-789",
    ]
    for number in sample_numbers:
        result = validate_us_phone(number)
        print(f"{number}: {result}")