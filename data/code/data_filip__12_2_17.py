import re

def is_valid_phone_number(phone_number):
    pattern = r'^[\d\s\-\(\)]*$'
    return bool(re.match(pattern, phone_number))

if __name__ == '__main__':
    sample_values = [
        "123-456-7890",
        "(123) 456-7890",
        "123 456 7890",
        "1234567890",
        "123-456-7890!",
        "abc-456-7890",
        "",
        "(",
        ")123",
        "123 (456) 789-0"
    ]
    for value in sample_values:
        print(is_valid_phone_number(value))