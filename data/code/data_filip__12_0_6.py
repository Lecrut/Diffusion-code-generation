import re

def is_e164_valid(phone_number):
    if not isinstance(phone_number, str):
        return False
    pattern = r'^\+[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    test_cases = [
        "+14155552671",
        "+442071838750",
        "123456",
        "+0123456789",
        "+12345678901234567890",
        "+8613800138000",
        "+33612345678"
    ]
    for number in test_cases:
        result = is_e164_valid(number)
        print(f"{number}: {result}")