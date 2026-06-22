import re

def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def remove_spaces(input_string):
    validate_input(input_string)
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    result = remove_spaces(sample_string)
    print(result)