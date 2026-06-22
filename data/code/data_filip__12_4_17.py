import re

def filter_valid_phone_numbers(phone_numbers):
    pattern = re.compile(r'^\d{10}$')
    return [number for number in phone_numbers if pattern.match(number)]

if __name__ == '__main__':
    sample_phone_numbers = [
        '1234567890',
        '123-456-7890',
        '123.456.7890',
        '(123) 456-7890',
        '123456789',
        '12345678901',
        '123456789a',
        '9876543210',
        '',
        '0000000000'
    ]
    valid_numbers = filter_valid_phone_numbers(sample_phone_numbers)
    print(valid_numbers)