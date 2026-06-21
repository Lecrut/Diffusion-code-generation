import re

def remove_whitespace(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    whitespace_pattern = r'\s+'
    cleaned_string = re.sub(whitespace_pattern, '', input_string)
    return cleaned_string

if __name__ == '__main__':
    sample_input = "Hello\tWorld\nThis is a test."
    result = remove_whitespace(sample_input)
    print(result)