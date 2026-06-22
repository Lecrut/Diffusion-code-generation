import re

def is_valid_input(input_string):
    if not isinstance(input_string, str) or input_string.strip() == "":
        raise ValueError("Input must be a non-empty string")
    return True

def remove_spaces(input_string):
    is_valid_input(input_string)
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    result = remove_spaces(sample_input)
    print(result)