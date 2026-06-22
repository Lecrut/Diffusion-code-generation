import re

def filter_phone_numbers(phone_numbers):
    pattern = re.compile(r'^\d{10}$')
    return [num for num in phone_numbers if pattern.match(num)]

if __name__ == '__main__':
    sample_numbers = [
        "1234567890",
        "123-456-7890",
        "123456789",
        "12345678901",
        "9876543210",
        "abc1234567",
        "1112223333",
        "4445556667",
        "1234 567 890",
        "0987654321"
    ]
    print(filter_phone_numbers(sample_numbers))