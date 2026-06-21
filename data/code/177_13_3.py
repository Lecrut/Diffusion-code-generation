def tokenize(input_str):
    tokens = input_str.split()
    return [token for token in tokens if token]

if __name__ == '__main__':
    sample_input = "  This   is  another test string with irregular whitespace.  "
    result = tokenize(sample_input)
    print(result)