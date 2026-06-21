def extract_first_item(input_tuple):
    first, *_rest = input_tuple
    return first

if __name__ == '__main__':
    sample_tuple = (42, "hello", 3.14, True)
    result = extract_first_item(sample_tuple)
    print(result)