import re

def is_valid_mobile(phone_number: str) -> bool:
    pattern = r"^\+?[1-9]\d{1,14}$"
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_number = "+12125551234"
    result = is_valid_mobile(sample_number)
    print(result)