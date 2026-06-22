import re

def validate_us_phone(number):
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    if re.match(pattern, number):
        digits = re.sub(r'\D', '', number)
        if len(digits) == 10:
            return True
        if len(digits) == 11 and digits.startswith('1'):
            return True
    return False

if __name__ == '__main__':
    samples = [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "1234567890",
        "11234567890",
        "123-45-6789",
        "invalid"
    ]
    for phone in samples:
        result = validate_us_phone(phone)
        print(f"{phone}: {result}")