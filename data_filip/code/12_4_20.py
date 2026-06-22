import re

def filter_phone_numbers(phone_list):
    pattern = re.compile(r'^\d{10}$')
    return [number for number in phone_list if pattern.match(number)]

if __name__ == '__main__':
    sample_numbers = ["1234567890", "123-456-7890", "9876543210", "55512345", "0987654321", "abc1234567", "12345678901"]
    result = filter_phone_numbers(sample_numbers)
    print(result)