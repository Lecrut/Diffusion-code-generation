import re

def filter_phone_numbers(numbers):
    pattern = r'^\d{10}$'
    return [num for num in numbers if re.match(pattern, num)]

if __name__ == '__main__':
    phone_list = [
        '1234567890',
        '123-456-7890',
        '(123) 456-7890',
        '0987654321',
        '123456789',
        '12345678901'
    ]
    result = filter_phone_numbers(phone_list)
    print(result)