import re

def filter_phone_numbers(phone_numbers):
    pattern = r'^\d{10}$'
    return [number for number in phone_numbers if re.match(pattern, number)]

if __name__ == '__main__':
    sample_numbers = [
        "1234567890",
        "123-456-7890",
        "(123) 456-7890",
        "123456789",
        "12345678901",
        "12345abc789",
        "9876543210"
    ]
    print(filter_phone_numbers(sample_numbers))