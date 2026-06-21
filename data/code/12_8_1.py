import re

def is_valid_mobile(number: str) -> bool:
    pattern = r'^\+?[1-9]\d{9,14}$'
    return bool(re.match(pattern, number))

if __name__ == '__main__':
    sample_numbers = ["+12025551234", "123456789", "+44 7911 123456", "abc123"]
    results = [is_valid_mobile(num) for num in sample_numbers]
    print(results)