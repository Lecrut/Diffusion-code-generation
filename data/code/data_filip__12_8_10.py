import re

def validate_mobile_number(phone_number):
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_numbers = [
        "+1234567890",
        "1234567890",
        "+44 123 456 7890",
        "123-456-7890",
        "abcdef12345",
        "+123456789012345",
        "123456789",
        "+49 176 12345678"
    ]
    for number in sample_numbers:
        print(validate_mobile_number(number))