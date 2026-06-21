import re

def filter_10_digit_phone_numbers(phone_numbers):
    pattern = re.compile(r'^\d{10}$')
    return [number for number in phone_numbers if pattern.match(number)]

if __name__ == '__main__':
    sample_numbers = [
        "1234567890",
        "123-456-7890",
        "123456789",
        "12345678901",
        "abcdefghij",
        "0987654321",
        "123 456 7890",
        "12345678901234",
        "2345678901",
        "34567890123"
    ]
    filtered_numbers = filter_10_digit_phone_numbers(sample_numbers)
    print(filtered_numbers)