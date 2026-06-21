def tokenize_string(input_string):
    return ' '.join(filter(str.isalpha, input_string)).split()

if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    print(tokenize_string(sample_input))