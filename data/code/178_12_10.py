def tokenize_string(input_str):
    return ' '.join(filter(str.isalpha, input_str)).split()

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    print(tokenize_string(sample_input))