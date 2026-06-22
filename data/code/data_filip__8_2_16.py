def split_and_strip_tokens(input_string):
    return [token.strip() for token in input_string.split(',')]

if __name__ == '__main__':
    sample_data = "  apple , banana ,  cherry , date  "
    result = split_and_strip_tokens(sample_data)
    print(result)