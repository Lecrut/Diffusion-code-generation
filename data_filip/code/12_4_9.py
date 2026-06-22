import re

def filter_phone_numbers(numbers):
    pattern = re.compile(r'^\d{10}$')
    return [number for number in numbers if pattern.match(number)]

if __name__ == '__main__':
    sample_numbers = ["1234567890", "123-456-7890", "9876543210", "abc1234567", "12345", "5555555555"]
    result = filter_phone_numbers(sample_numbers)
    print(result)