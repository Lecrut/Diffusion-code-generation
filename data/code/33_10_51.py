import re

def remove_whitespace(input_string):
    whitespace_pattern = '\\s+'
    compiled_pattern = re.compile(whitespace_pattern)
    cleaned_string = compiled_pattern.sub('', input_string)
    return cleaned_string
if __name__ == '__main__':
    sample_input = '   This\texample\nstring contains  multiple \t types of whitespace.   '
    result = remove_whitespace(sample_input)
    print(result)