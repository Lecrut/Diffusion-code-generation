import re

def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def split_string_efficiently(text):
    validate_input(text)
    return re.split(r'\s+', text)

if __name__ == '__main__':
    input_string = "  This   is a test string with multiple spaces "
    result = split_string_efficiently(input_string)
    print(result)