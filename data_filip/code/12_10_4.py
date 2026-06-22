import re

_phone_pattern = re.compile(r'^\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}$')

def validate_phone(phone_number: str) -> bool:
    return bool(_phone_pattern.match(phone_number))

if __name__ == '__main__':
    test_cases = [
        "1234567890",
        "123-456-7890",
        "(123) 456-7890",
        "(123)456-7890",
        "123 456 7890",
        "123-45-6789",
        "12-3456-7890",
        "12345678901"
    ]
    
    for number in test_cases:
        print(validate_phone(number))