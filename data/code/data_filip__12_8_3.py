import re

def validate_mobile_phone(phone_number):
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_numbers = [
        "+1234567890",
        "1234567890",
        "+98765432101234",
        "123-456-7890",
        "+01234567890",
        "12345",
        "+123456789012345",
        "abc1234567"
    ]
    for num in sample_numbers:
        print(f"{num}: {validate_mobile_phone(num)}")