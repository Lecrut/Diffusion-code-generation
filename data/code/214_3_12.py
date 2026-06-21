def find_min_in_tuple(input_tuple):
    if not isinstance(input_tuple, tuple) or not all(isinstance(x, int) for x in input_tuple):
        raise ValueError("Input must be a non-empty tuple of integers.")
    return min(input_tuple)

if __name__ == '__main__':
    sample_tuple_1 = (5, 2, 8, 1, 9)
    try:
        min_1 = find_min_in_tuple(sample_tuple_1)
        print(min_1)
    except ValueError as e:
        print(e)