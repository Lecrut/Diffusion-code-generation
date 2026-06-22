import re

def validate_phone_number(phone_number: str) -> bool:
    pattern = r'^\+?1?\d{9,15}$'
    cleaned = re.sub(r'[\s\-\(\)]', '', phone_number)
    return bool(re.match(pattern, cleaned))

if __name__ == '__main__':
    phone_numbers = [
        "+1-555-0199",
        "555.0199",
        "invalid-phone",
        "+44 20 7946 0958",
        "123",
        "+86 13800138000"
    ]
    for number in phone_numbers:
        result = validate_phone_number(number)
        print(result)