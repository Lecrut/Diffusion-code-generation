import re

def filter_valid_phone_numbers(phone_list):
    pattern = re.compile(r'^\d{10}$')
    return [num for num in phone_list if pattern.match(num)]

if __name__ == '__main__':
    sample_numbers = [
        '1234567890',
        '0987654321',
        '123',
        '12345678901',
        '1234567890',
        'abcdefghij',
        '123456789',
        '1234567890'
    ]
    valid_numbers = filter_valid_phone_numbers(sample_numbers)
    print(valid_numbers)