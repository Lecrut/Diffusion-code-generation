import re

def validate_e164(phone_number: str) -> bool:
    pattern = r'^\+[1-9]\d{0,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    test_numbers = [
        "+12025551234",
        "+442071838750",
        "+15551234567890123",
        "12025551234",
        "+120255512345",
        "+012025551234",
        "+1-202-555-1234",
        "+8613800138000",
        "+1"
    ]
    for number in test_numbers:
        print(validate_e164(number))