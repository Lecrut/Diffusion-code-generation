import re

def tokenize_string(input_string):
    return [token for token in re.split(r'\W+', input_string) if token]

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test."
    print(tokenize_string(sample_string))