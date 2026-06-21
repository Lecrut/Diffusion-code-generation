def extract_first_item(t):
    first, *_ = t
    return first

if __name__ == '__main__':
    sample_tuple = (42, 'hello', 3.14, True)
    result = extract_first_item(sample_tuple)
    print(result)