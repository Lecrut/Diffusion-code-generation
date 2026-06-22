import re

def is_e164_valid(phone_number):
    if not isinstance(phone_number, str):
        return False
    pattern = r'^\+[1-9]\d{0,14}$'
    return bool(re.fullmatch(pattern, phone_number))

if __name__ == '__main__':
    test_cases = [
        "+12025551234",
        "+442079460018",
        "+8613800138000",
        "12025551234",
        "+123456789012345678",
        "+0123456789",
        "abc",
        "+1",
        "+12",
        "+123",
        "+1234567890123456789"
    ]
    for case in test_cases:
        print(f"{case}: {is_e164_valid(case)}")