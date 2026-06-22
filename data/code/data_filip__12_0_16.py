import re

def validate_e164(phone_number):
    pattern = r'^\+[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    test_numbers = [
        "+1234567890",
        "+447911123456",
        "+123",
        "1234567890",
        "+01234567890",
        "+447911123456789012345"
    ]
    for number in test_numbers:
        print(validate_e164(number))