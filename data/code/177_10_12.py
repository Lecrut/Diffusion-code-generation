import re

def split_string(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return re.split(r'\s+', text)

if __name__ == '__main__':
    input_string = "  This   is a test string with multiple spaces "
    try:
        result = split_string(input_string)
        print(result)
    except ValueError as e:
        print(e)