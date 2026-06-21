import re

def validate_phone_number(phone_number):
    pattern = r'^[\d\s\-\(\)]+$'
    if not phone_number:
        return False
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    samples = ["(123) 456-7890", "123-456-7890", "123 456 7890", "1234567890", "123-45-6789", "12345", "123-abc-7890", "", "   ", "(123] 456-7890"]
    for sample in samples:
        print(validate_phone_number(sample))