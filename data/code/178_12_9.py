def tokenize_string(input_string):
    import re
    return re.findall(r'\b\w+\b', input_string)

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    print(tokenize_string(sample_input))