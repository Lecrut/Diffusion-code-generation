import re

def validate_phone_number(phone: str) -> bool:
    if len(phone) < 7 or len(phone) > 15:
        return False
    return not bool(re.search(r'[a-zA-Z]', phone))

if __name__ == '__main__':
    samples = [
        "1234567",
        "123456789012345",
        "123456",
        "1234567890123456",
        "12345678",
        "12345678a",
        "123456789012345!",
        "123-456-7890",
        "123 456 7890"
    ]
    
    for sample in samples:
        result = validate_phone_number(sample)
        print(result)