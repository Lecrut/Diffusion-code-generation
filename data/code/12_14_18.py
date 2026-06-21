import re

PHONE_NUMBERS = [
    "+1-212-555-0199",
    "212 555 0199",
    "(212) 555-0199",
    "12125550199",
    "212.555.0199",
    "invalid-number",
    "+44 20 7946 0958",
    "123-abc-4567",
    "+86 10 1234 5678",
    "001 212 555 0199"
]

def validate_phone_format(phone_string: str) -> bool:
    pattern = r"^\+?[\d\s\-\.\(\)]{7,15}$"
    return bool(re.match(pattern, phone_string))

if __name__ == '__main__':
    results = [validate_phone_format(num) for num in PHONE_NUMBERS]
    for number, is_valid in zip(PHONE_NUMBERS, results):
        print(is_valid)