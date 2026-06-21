import re

def validate_us_phone_number(phone):
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, phone))

if __name__ == '__main__':
    test_cases = [
        "(123) 456-7890",
        "123-456-7890",
        "1234567890",
        "123.456.7890",
        "123 456 7890",
        "(123)456-7890",
        "123-45-6789",
        "123-456-789",
        "abc-def-ghij"
    ]
    
    for number in test_cases:
        result = validate_us_phone_number(number)
        print(f"{number}: {result}")