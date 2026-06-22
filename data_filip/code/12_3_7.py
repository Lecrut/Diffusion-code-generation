import re

def validate_us_phone(phone_number):
    pattern = r'^\(?([2-9]\d{2})\)?[\s.-]?([2-9]\d{2})[\s.-]?(\d{4})$'
    match = re.match(pattern, phone_number)
    return bool(match)

if __name__ == '__main__':
    samples = [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "123 456 7890",
        "1234567890",
        "(023) 456-7890",
        "(123) 056-7890",
        "123-45-67890",
        "abc-def-ghij",
        "+1 123 456 7890"
    ]
    for sample in samples:
        print(validate_us_phone(sample))