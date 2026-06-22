def compare_arrays_at_positions(arr_a, arr_b, positions):
    if not isinstance(arr_a, (list, tuple)):
        raise ValueError("First argument must be a list or tuple")
    if not isinstance(arr_b, (list, tuple)):
        raise ValueError("Second argument must be a list or tuple")
    if not isinstance(positions, (list, tuple, set)):
        raise ValueError("Positions must be an iterable of integers")
    for pos in positions:
        if not isinstance(pos, int):
            raise ValueError("Each position must be an integer")
    matches = 0
    for pos in positions:
        if pos < 0 or pos >= len(arr_a) or pos >= len(arr_b):
            continue
        if arr_a[pos] == arr_b[pos]:
            matches += 1
    return matches

if __name__ == '__main__':
    array_one = [1, 2, 3, 4, 5]
    array_two = [1, 9, 3, 8, 5]
    check_positions = [0, 2, 4]
    result = compare_arrays_at_positions(array_one, array_two, check_positions)
    print(result)