def extract_first_item(t):
    first, *_ = t
    return first

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = extract_first_item(sample_tuple)
    print(result)