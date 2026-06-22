import re

def validate_mobile_number(number):
    pattern = r'^\+?1?\s?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, number))

if __name__ == '__main__':
    sample_number = "(555) 123-4567"
    print(validate_mobile_number(sample_number))