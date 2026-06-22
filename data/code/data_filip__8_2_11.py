def split_and_strip(s):
    return [token.strip() for token in s.split(',')]

if __name__ == '__main__':
    sample_string = "  apple , banana ,  cherry  , date "
    result = split_and_strip(sample_string)
    print(result)