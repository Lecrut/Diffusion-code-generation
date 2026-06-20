def strip_tuple_whitespace(input_tuple):
    cleaned = tuple(s.strip() for s in input_tuple)
    return cleaned

if __name__ == '__main__':
    sample_data = ('  hello  ', 'world ', ' python ', '  ')
    result = strip_tuple_whitespace(sample_data)
    print(result)