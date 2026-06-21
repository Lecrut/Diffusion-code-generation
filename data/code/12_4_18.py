import re

def filter_phone_numbers(phone_list):
    pattern = re.compile(r'^[0-9]{10}$')
    return [number for number in phone_list if pattern.match(number)]

if __name__ == '__main__':
    sample_numbers = ["1234567890", "555-555-5555", "0987654321", "123", "1111111111", "+1 (234) 567-890"]
    result = filter_phone_numbers(sample_numbers)
    print(result)