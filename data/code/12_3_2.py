import re

def validate_us_phone_number(phone):
    pattern = r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

if __name__ == '__main__':
    test_numbers = [
        "(123) 456-7890",
        "123-456-7890",
        "1234567890",
        "(12) 3456-7890",
        "123-45-67890"
    ]
    
    for number in test_numbers:
        result = validate_us_phone_number(number)
        print(f"{number}: {result}")