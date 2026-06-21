import re

def validate_phone_number(phone_number: str) -> bool:
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    phone_numbers = [
        "+1234567890",
        "1234567890",
        "+0000000000",
        "123-456-7890",
        "+12",
        "abc123",
        "+123456789012345",
        "123456789012345"
    ]
    for number in phone_numbers:
        result = validate_phone_number(number)
        print(result)