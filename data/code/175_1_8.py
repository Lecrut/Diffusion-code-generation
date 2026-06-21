import re

def tokenize_string(input_str):
    return re.findall(r'\b\w+\b', input_str)

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    print(tokenize_string(sample_input))