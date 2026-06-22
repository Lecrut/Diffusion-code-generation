import re

def validate_phone(phone_number: str) -> bool:
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.fullmatch(pattern, phone_number))

if __name__ == '__main__':
    number = "+12065550199"
    print(validate_phone(number))