def split_tokens(input_string):
    return input_string.split()

if __name__ == '__main__':
    sample_input = "  This   is  a test string  with irregular whitespace  "
    tokens = split_tokens(sample_input)
    print(tokens)