import re

def filter_phone_numbers(phone_list):
    pattern = re.compile(r'^\d{10}$')
    return [number for number in phone_list if pattern.match(number)]

if __name__ == '__main__':
    sample_numbers = [
        "1234567890",
        "555-123-4567",
        "9876543210",
        "123",
        "0987654321",
        "1112223333",
        "abc123def456",
        "2223334444"
    ]
    result = filter_phone_numbers(sample_numbers)
    print(result)