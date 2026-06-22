import re

def validate_phone_number(phone_number: str) -> bool:
    pattern = r"^\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}$"
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    samples = [
        "(123) 456-7890",
        "123-456-7890",
        "1234567890",
        "(123)456-7890",
        "123 456 7890",
        "invalid",
        "123-45-6789"
    ]
    for sample in samples:
        print(f"{sample}: {validate_phone_number(sample)}")