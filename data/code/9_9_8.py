def strip_tuple_strings(input_tuple):
    return tuple(s.strip() for s in input_tuple)

if __name__ == '__main__':
    sample_data = ("  hello  ", "  world  ", "  foo  ")
    result = strip_tuple_strings(sample_data)
    print(result)