import re

def validate_phone_number(phone: str) -> bool:
    pattern = r"^\+?1?\s*\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.match(pattern, phone))

if __name__ == "__main__":
    sample_numbers = ["(555) 123-4567", "555-987-6543", "123", "555.222.3333"]
    for number in sample_numbers:
        result = validate_phone_number(number)
        print(f"{number}: {result}")