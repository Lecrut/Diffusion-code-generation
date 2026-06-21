def tokenize_string(input_str):
    tokens = input_str.split()
    return [token for token in tokens if token]

if __name__ == '__main__':
    sample_input = "  This   is  yet another test string with irregular whitespace.  "
    result = tokenize_string(sample_input)
    print(result)