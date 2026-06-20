def strip_tuple_whitespace(input_tuple):
    return tuple(s.strip() for s in input_tuple)

if __name__ == '__main__':
    sample_data = ('  hello  ', ' world ', ' foo  bar ')
    result = strip_tuple_whitespace(sample_data)
    print(result)