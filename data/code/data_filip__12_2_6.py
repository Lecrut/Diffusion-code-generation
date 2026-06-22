import re

def is_valid_phone_number(phone: str) -> bool:
    pattern = r'^[\d\s\-\(\)]+$'
    return bool(re.match(pattern, phone))

if __name__ == '__main__':
    sample_phone_numbers = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "123.456.7890",
        "abc-def-ghij",
        "1234567890",
        ""
    ]

    for phone in sample_phone_numbers:
        result = is_valid_phone_number(phone)
        print(f"{phone}: {result}")