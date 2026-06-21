def extract_first_item(tuple_item):
    first, *rest = tuple_item
    return first

if __name__ == '__main__':
    sample_tuple = (42, "hello", [1, 2, 3])
    result = extract_first_item(sample_tuple)
    print(result)