import re

def tokenize_string(input_string):
    return re.findall(r'\b\w+\b', input_string)

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string with some numbers 123 and symbols @#$."
    print(tokenize_string(sample_string))