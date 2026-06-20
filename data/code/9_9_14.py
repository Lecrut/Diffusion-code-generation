def strip_tuple_whitespace(input_tuple):
    return tuple(item.strip() for item in input_tuple)

if __name__ == '__main__':
    sample_data = ("  hello  ", "  world  ", "   ", "  python  ")
    result = strip_tuple_whitespace(sample_data)
    print(result)