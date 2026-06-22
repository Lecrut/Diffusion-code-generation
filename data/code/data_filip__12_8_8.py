import re
import sys

def validate_phone(phone):
    pattern = r'^\+?[1-9]\d{9,14}$'
    return bool(re.match(pattern, phone))

if __name__ == '__main__':
    sample_number = "+12025551234"
    result = validate_phone(sample_number)
    print(result)