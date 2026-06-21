import re

def is_e164(phone: str) -> bool:
    pattern = r'^\+[1-9]\d{1,14}$'
    return bool(re.fullmatch(pattern, phone))

if __name__ == '__main__':
    test_numbers = [
        "+12025551234",
        "+442079460018",
        "+8613800138000",
        "12025551234",
        "+1-202-555-1234",
        "+0123456789",
        "+12345678901234567890",
        "+1"
    ]
    
    for number in test_numbers:
        result = is_e164(number)
        print(f"{number}: {result}")