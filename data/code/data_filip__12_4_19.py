import re

def filter_phone_numbers(phone_list):
    pattern = re.compile(r'^\d{10}$')
    return [num for num in phone_list if pattern.match(num)]

if __name__ == '__main__':
    phones = [
        '1234567890',
        '123-456-7890',
        '12345678901',
        '123456789',
        '9876543210',
        '0000000000'
    ]
    result = filter_phone_numbers(phones)
    print(result)