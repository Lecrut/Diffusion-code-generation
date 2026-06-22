import re

def validate_us_phone_number(phone_number: str) -> bool:
    pattern = r'^\s*\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\s*$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_numbers = ["(123) 456-7890", "123-456-7890", "123.456.7890", "1234567890", "123-45-6789", "(123)4567890"]
    results = [validate_us_phone_number(number) for number in sample_numbers]
    for number, is_valid in zip(sample_numbers, results):
        print(f"{number}: {is_valid}")