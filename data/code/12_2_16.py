import re

def validate_phone_number(phone_number):
    allowed_pattern = re.compile(r'^[0-9\s\-\(\)]+$')
    return bool(allowed_pattern.match(phone_number))

if __name__ == '__main__':
    samples = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "1234567890",
        "123-456-7890!",
        "abc-def-ghij",
        "(123)456-7890",
        "123-456-7890 ext. 123",
        "+1 123 456 7890",
        ""
    ]
    for sample in samples:
        print(validate_phone_number(sample))