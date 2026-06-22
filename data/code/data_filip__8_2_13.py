def split_and_strip(text):
    return [token.strip() for token in text.split(',')]

if __name__ == '__main__':
    sample_string = " apple , banana , cherry "
    result = split_and_strip(sample_string)
    print(result)