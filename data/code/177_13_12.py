def split_non_empty_tokens(input_string):
    return [token for token in input_string.split() if token]

if __name__ == '__main__':
    sample_input = "  This   is  a test string with irregular whitespace.  "
    tokens = split_non_empty_tokens(sample_input)
    print(tokens)