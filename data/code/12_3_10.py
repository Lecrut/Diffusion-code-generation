import re

def validate_us_phone_number(phone: str) -> bool:
    pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.match(pattern, phone))

if __name__ == "__main__":
    samples = ["(123) 456-7890", "123-456-7890", "123.456.7890", "1234567890", "123 456 7890", "invalid", "1234-567-8901"]
    for sample in samples:
        result = validate_us_phone_number(sample)
        print(result)