import re

def is_alphanumeric(input_string):
    pattern = r'^\w+$'
    return bool(re.match(pattern, input_string))

if __name__ == '__main__':
    sample_values = [
        "Hello123",
        "World!",
        "Python3.8",
        "123456",
        "Test-Case"
    ]
    for value in sample_values:
        print(f"'{value}': {is_alphanumeric(value)}")