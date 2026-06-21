import re

def validate_us_phone(phone_number):
    cleaned = re.sub(r'[\s\-\(\)]', '', phone_number)
    if cleaned.startswith('+1'):
        cleaned = cleaned[2:]
    pattern = r'^\d{10}$'
    if re.match(pattern, cleaned):
        area = cleaned[:3]
        exchange = cleaned[3:6]
        subscriber = cleaned[6:]
        if area[0] != '0' and area[0] != '1':
            if exchange[0] != '0' and exchange[0] != '1':
                return True
    return False

if __name__ == '__main__':
    samples = [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "1234567890",
        "+11234567890",
        "123-056-7890",
        "123-156-7890",
        "023-456-7890",
        "123-456-789",
        "123-456-78901",
        "abc-def-ghij"
    ]
    for sample in samples:
        print(validate_us_phone(sample))