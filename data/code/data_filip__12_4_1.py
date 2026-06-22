import re

def filter_phone_numbers(phone_list):
    pattern = re.compile(r'^\d{10}$')
    return [phone for phone in phone_list if pattern.match(phone)]

if __name__ == '__main__':
    sample_numbers = [
        "1234567890",
        "123-456-7890",
        "9876543210",
        "12345",
        "9999999999",
        "abc1234567",
        "1111111111"
    ]
    print(filter_phone_numbers(sample_numbers))