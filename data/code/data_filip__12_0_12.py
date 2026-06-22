import re

def is_valid_e164(phone_number: str) -> bool:
    pattern = r'^\+[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_phones = [
        "+12065551234",
        "+447911123456",
        "+8613800138000",
        "+120655512345",
        "12065551234",
        "+0001234567890",
        "+12065551234",
    ]
    
    for phone in sample_phones:
        result = is_valid_e164(phone)
        print(result)