import re

def validate_us_phone_number(phone_number: str) -> bool:
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    test_cases = [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "1234567890",
        "123 456 7890",
        "(123)456-7890",
        "12-345-6789",
        "123-45-6789",
        "abc-def-ghij",
        "123-456-78901"
    ]
    
    results = {}
    for number in test_cases:
        results[number] = validate_us_phone_number(number)
    
    for number, is_valid in results.items():
        print(f"{number}: {is_valid}")