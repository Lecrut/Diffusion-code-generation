import re

def filter_phone_numbers(phone_numbers):
    pattern = re.compile(r'^\d{10}$')
    return [num for num in phone_numbers if pattern.match(num)]

if __name__ == '__main__':
    numbers = ['1234567890', '123', '0987654321', '111-222-3333', '4445556666', 'abcde12345']
    result = filter_phone_numbers(numbers)
    print(result)