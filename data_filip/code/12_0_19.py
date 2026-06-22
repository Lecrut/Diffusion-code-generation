import re

def validate_e164(phone_number: str) -> bool:
    pattern = r'^\+[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    samples = [
        "+12025551234",
        "+447911123456",
        "+919876543210",
        "12025551234",
        "+012025551234",
        "+1202555123",
        "invalid",
        "+12025551234567"
    ]
    for s in samples:
        result = validate_e164(s)
        print(result)