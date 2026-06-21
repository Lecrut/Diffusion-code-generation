import re

def validate_us_phone(number):
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, str(number)))

if __name__ == '__main__':
    print(validate_us_phone("(123) 456-7890"))
    print(validate_us_phone("123-456-7890"))
    print(validate_us_phone("1234567890"))
    print(validate_us_phone("123 456 7890"))
    print(validate_us_phone("123-456-789"))