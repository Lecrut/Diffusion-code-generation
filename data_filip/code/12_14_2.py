import re

def validate_phone_number(phone_number: str) -> bool:
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    phone_numbers = [
        "+1234567890",
        "123-456-7890",
        "+44 20 7946 0958",
        "1234567890",
        "+8613812345678",
        "invalid",
        "+01234567890",
        "+123"
    ]
    for number in phone_numbers:
        print(validate_phone_number(number))