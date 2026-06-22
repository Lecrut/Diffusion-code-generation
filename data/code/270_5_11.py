import re

def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string

def remove_spaces(input_string):
    validated_string = validate_input(input_string)
    return re.sub(r'\s+', '', validated_string)

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    result = remove_spaces(sample_string)
    print(result)