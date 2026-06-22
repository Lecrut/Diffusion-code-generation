def extract_first_item(tup):
    first, *_ = tup
    return first

if __name__ == '__main__':
    sample_tuple = (42, 'hello', 3.14)
    result = extract_first_item(sample_tuple)
    print(result)