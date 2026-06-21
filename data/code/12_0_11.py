import re

def is_valid_e164(phone_number):
    if not isinstance(phone_number, str):
        return False
    pattern = re.compile(r'^\+[1-9]\d{1,14}$')
    return bool(pattern.match(phone_number))

if __name__ == '__main__':
    test_numbers = ["+14155552671", "+442071838750", "+123", "+9999999999999999", "123456", "+1-415-555-2671", "+44 20 7183 8750", "+"]
    for number in test_numbers:
        print(is_valid_e164(number))