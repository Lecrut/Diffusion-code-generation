def strip_whitespace(string_list):
    return [s.strip() for s in string_list]

if __name__ == '__main__':
    sample = ['  hello  ', 'world ', '  test', '   ', 'no_spaces']
    print(strip_whitespace(sample))