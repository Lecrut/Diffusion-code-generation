import re

def is_e164_valid(phone_number):
    if not isinstance(phone_number, str):
        return False
    e164_pattern = re.compile(r'^\+[1-9]\d{1,14}$')
    return bool(e164_pattern.match(phone_number))

if __name__ == '__main__':
    test_cases = ["+12025551234", "+442079460123", "+8613800138000", "12025551234", "+123", "+", "+12345678901234567"]
    results = [is_e164_valid(number) for number in test_cases]
    for original, result in zip(test_cases, results):
        print(f"{original}: {result}")