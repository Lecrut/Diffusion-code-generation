def tokenize_string(input_str):
    return [token for token in input_str.split() if token]

if __name__ == '__main__':
    sample_input = "  This   is a test string with  irregular whitespace.  "
    print(tokenize_string(sample_input))