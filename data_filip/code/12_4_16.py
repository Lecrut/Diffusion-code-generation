import re

def filter_phone_numbers(phone_numbers):
    pattern = re.compile(r'^\d{10}$')
    return [number for number in phone_numbers if pattern.match(number)]

if __name__ == '__main__':
    sample_numbers = [
        "1234567890",
        "123-456-7890",
        "(123) 456-7890",
        "123456789",
        "12345678901",
        "abc1234567",
        "0987654321",
        "1111111111",
        "2222222222a",
        "3333333333"
    ]
    result = filter_phone_numbers(sample_numbers)
    print(result)