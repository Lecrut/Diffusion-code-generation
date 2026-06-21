import re

def tokenize_string(input_string):
    words = re.findall(r'\b\w+\b', input_string)
    return words

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with some numbers 123 and symbols $#@."
    print(tokenize_string(sample_string))