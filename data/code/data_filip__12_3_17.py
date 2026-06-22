import re

def validate_us_phone(phone):
    pattern = r'^(\d{3}[-.\s]\d{3}[-.\s]\d{4}|[\(]\d{3}[\)][\s.-]?\d{3}[-.\s]\d{4})$'
    return bool(re.match(pattern, phone.strip()))

if __name__ == '__main__':
    samples = [
        '(123) 456-7890',
        '123-456-7890',
        '123.456.7890',
        '123 456 7890',
        '(123)456-7890',
        '123-456-789',
        '1234567890',
        '(123) 456-789',
        'abc-def-ghij'
    ]
    for sample in samples:
        print(validate_us_phone(sample))