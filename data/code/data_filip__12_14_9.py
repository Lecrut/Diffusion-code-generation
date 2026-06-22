import re

def validate_phone_number(phone: str) -> bool:
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone))

if __name__ == '__main__':
    phone_numbers = [
        "+1234567890",
        "1234567890",
        "+01234567890",
        "abc123",
        "",
        "+12",
        "1234567890123456"
    ]
    for number in phone_numbers:
        result = validate_phone_number(number)
        print(result)