import re

E164_PATTERN = re.compile(r'^\+[1-9]\d{1,14}$')

def is_valid_e164(phone_number):
    if not isinstance(phone_number, str):
        return False
    return bool(E164_PATTERN.match(phone_number))

if __name__ == '__main__':
    test_cases = ["+14155552671", "+442071838750", "+4420 7183 8750", "+123", "+12345678901234567890", "+01234567890", "+11234567890", "+1234567890", "+8613800138000", "1234567890", "+99912345678901234567"]
    for number in test_cases:
        result = is_valid_e164(number)
        print(f"{number}: {result}")