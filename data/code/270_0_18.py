import re

def remove_spaces(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    try:
        result = remove_spaces(sample_input)
        print(result)
    except ValueError as e:
        print(e)