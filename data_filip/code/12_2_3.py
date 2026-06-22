import re

def validate_phone_number(phone_number):
    return bool(re.match(r'^[\d\s\-\(\)]+$', phone_number))

if __name__ == '__main__':
    samples = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "1234567890",
        "abc-def-ghij",
        "123-456-789!",
        "(123)456-7890",
        "   ",
        "-",
        "()",
        "123 456 7890 x123"
    ]
    for sample in samples:
        result = validate_phone_number(sample)
        print(result)