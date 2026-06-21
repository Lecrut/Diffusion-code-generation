import re

def filter_phone_numbers(phone_list):
    pattern = re.compile(r'^\d{10}$')
    return [phone for phone in phone_list if pattern.match(phone)]

if __name__ == '__main__':
    sample_numbers = ["1234567890", "987-654-3210", "5551234567", "12345", "9998887777", "abc1234567", "0000000000"]
    filtered_result = filter_phone_numbers(sample_numbers)
    print(filtered_result)