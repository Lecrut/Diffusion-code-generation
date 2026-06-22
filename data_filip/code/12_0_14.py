import re

def validate_e164(phone_number: str) -> bool:
    pattern = r'^\+[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_numbers = ["+1234567890", "+11234567890", "+1", "+01234567890", "1234567890", "+12345678901"]
    for num in sample_numbers:
        result = validate_e164(num)
        print(result)