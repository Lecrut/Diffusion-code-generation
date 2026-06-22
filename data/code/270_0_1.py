import re

def remove_spaces(input_string):
    return re.sub(r'\s+', '', input_string)

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    result = remove_spaces(sample_input)
    print(result)