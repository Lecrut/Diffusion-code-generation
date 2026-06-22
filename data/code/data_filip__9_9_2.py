def strip_tuple_strings(data):
    return tuple(item.strip() for item in data)

if __name__ == '__main__':
    sample_data = ("  hello  ", " world ", "  python ", "  ")
    result = strip_tuple_strings(sample_data)
    print(result)