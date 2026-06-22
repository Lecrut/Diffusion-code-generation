def strip_tuple_strings(input_tuple):
    return tuple(item.strip() for item in input_tuple)

if __name__ == '__main__':
    sample_data = ("  hello  ", " world ", "python")
    result = strip_tuple_strings(sample_data)
    print(result)