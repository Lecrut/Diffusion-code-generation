def split_and_strip(string_value):
    return [token.strip() for token in string_value.split(',')]

if __name__ == '__main__':
    sample_input = "  apple, banana ,  cherry, date  , fig"
    result = split_and_strip(sample_input)
    print(result)