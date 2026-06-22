import re

def is_valid_e164(phone_number: str) -> bool:
    if not isinstance(phone_number, str):
        return False
    pattern = re.compile(r'^\+[1-9]\d{1,14}$')
    return bool(pattern.match(phone_number))

if __name__ == '__main__':
    test_cases = [
        "+12025550123",
        "+442071838750",
        "+123",
        "1234567890",
        "+1-202-555-0123",
        "+919876543210",
        "+1 202 555 0123",
        "+6281234567890"
    ]
    for number in test_cases:
        print(is_valid_e164(number))