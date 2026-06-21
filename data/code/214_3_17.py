def find_min_in_tuple(data):
    if not isinstance(data, tuple) or not all((isinstance(x, int) for x in data)):
        raise ValueError('Input must be a non-empty tuple of integers.')
    if len(data) == 0:
        raise ValueError('Tuple cannot be empty.')
    min_val = data[0]
    for val in data[1:]:
        if val < min_val:
            min_val = val
    return min_val
if __name__ == '__main__':
    sample_tuple_1 = (5, 2, 8, 1, 9)
    try:
        min_1 = find_min_in_tuple(sample_tuple_1)
        print(min_1)
    except ValueError as e:
        print(e)
    sample_tuple_2 = ()
    try:
        min_2 = find_min_in_tuple(sample_tuple_2)
        print(min_2)
    except ValueError as e:
        print(e)
    sample_tuple_3 = (5, 'a', 8, 1, 9)
    try:
        min_3 = find_min_in_tuple(sample_tuple_3)
        print(min_3)
    except ValueError as e:
        print(e)