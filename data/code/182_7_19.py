import re

def validate_input(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

def separate_characters(input_string):
    validate_input(input_string)
    return list(re.findall(r'\b', input_string))

if __name__ == '__main__':
    sample_string = "Hello123World!"
    result = separate_characters(sample_string)
    print(result)