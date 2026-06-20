def split_and_strip(input_string):
    return [token.strip() for token in input_string.split(',')]

if __name__ == '__main__':
    sample_data = "  apple  , banana ,  cherry ,date  "
    result = split_and_strip(sample_data)
    print(result)