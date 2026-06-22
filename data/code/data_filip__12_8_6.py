import re

validate_phone = lambda phone: bool(re.match(r'^\+?1?\d{9,15}$', phone))

if __name__ == '__main__':
    sample_numbers = [
        "+1234567890",
        "1234567890",
        "+44123456789",
        "123-456-7890",
        "+12345",
        "abcdefghijk"
    ]
    results = {num: validate_phone(num) for num in sample_numbers}
    print(results)