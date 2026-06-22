import re

PHONE_PATTERN = r'^\+?1?\d{9,15}$'

def validate_phone_format(phone_number: str) -> bool:
    return bool(re.match(PHONE_PATTERN, phone_number))

if __name__ == '__main__':
    phones = [
        "+1234567890",
        "123456789",
        "123-456-7890",
        "+9876543210",
        "invalid_phone",
        "+123456789012345"
    ]
    results = [validate_phone_format(p) for p in phones]
    for phone, is_valid in zip(phones, results):
        print(f"{phone}: {is_valid}")