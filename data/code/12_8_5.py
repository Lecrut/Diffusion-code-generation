import re

def validate_phone_number(number: str) -> bool:
    pattern = r'^\+?1?\s*\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$'
    return bool(re.match(pattern, number))

if __name__ == '__main__':
    sample_numbers = ["(555) 123-4567", "+1-800-555-0199", "123", "5551234567"]
    for number in sample_numbers:
        result = validate_phone_number(number)
        print(f"{number}: {result}")