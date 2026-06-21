def find_min_element(data):
    if not isinstance(data, tuple) or not all(isinstance(x, int) for x in data):
        raise ValueError("Input must be a tuple of integers")
    if not data:
        return None
    min_val = data[0]
    for val in data[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_tuple_1 = (5, 2, 8, 1, 9)
    min_1 = find_min_element(sample_tuple_1)
    print(min_1)