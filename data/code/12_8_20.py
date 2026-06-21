import re

validate_mobile = lambda phone: bool(re.match(r'^\+?1?\d{9,15}$', phone))

if __name__ == '__main__':
    sample_numbers = ["+1234567890", "1234567890", "+44123456789", "123-456-7890", "abc123"]
    for number in sample_numbers:
        print(validate_mobile(number))