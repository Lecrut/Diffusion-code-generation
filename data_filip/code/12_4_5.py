import re

def filter_valid_phone_numbers(phone_numbers):
    pattern = re.compile(r'^\d{10}$')
    return [number for number in phone_numbers if pattern.match(number)]

if __name__ == '__main__':
    sample_numbers = [
        "1234567890",
        "123-456-7890",
        "123456789",
        "12345678901",
        "123456789a",
        "(123) 456-7890",
        "0987654321",
        "123 456 7890",
        "5551234567",
        "abc1234567",
        "12345678901234",
        "9876543210",
        "123456789!",
        "123456789",
        "1234567890"
    ]
    result = filter_valid_phone_numbers(sample_numbers)
    print(result)