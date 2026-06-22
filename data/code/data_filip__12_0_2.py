import re

def is_valid_e164(phone_number):
    if not isinstance(phone_number, str):
        return False
    pattern = r'^\+[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_numbers = [
        "+12025551234",
        "+442079460018",
        "+12125551234",
        "+919876543210",
        "12025551234",
        "+1-202-555-1234",
        "0012025551234",
        "+0",
        "+12345678901234567890",
        "+1234567890"
    ]
    for number in sample_numbers:
        result = is_valid_e164(number)
        print(f"{number}: {result}")