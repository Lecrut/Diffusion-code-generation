def split_tokens(input_string):
    return [token for token in input_string.split() if token]

if __name__ == '__main__':
    sample_input = "  This   is  a test string with irregular whitespace.  "
    print(split_tokens(sample_input))