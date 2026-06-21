import re

def is_valid_mobile(phone_number: str) -> bool:
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_numbers = [
        "+1234567890",
        "1234567890",
        "+911234567890",
        "123",
        "+01234567890",
        "abc1234567890",
        ""
    ]
    for num in sample_numbers:
        print(is_valid_mobile(num))