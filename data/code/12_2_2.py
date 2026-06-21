import re

def is_valid_phone_number(phone: str) -> bool:
    pattern = r'^[\d\s\-\(\)]+$'
    return bool(re.match(pattern, phone))

if __name__ == '__main__':
    test_numbers = [
        "(123) 456-7890",
        "123-456-7890",
        "123 456 7890",
        "1234567890",
        "123-456-789",
        "abc-def-ghij",
        "123 456 7890 1234"
    ]
    for number in test_numbers:
        result = is_valid_phone_number(number)
        print(result)