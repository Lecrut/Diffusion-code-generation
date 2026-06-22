def find_largest_valid_int(data_tuple):
    valid_ints = [x for x in data_tuple if isinstance(x, int) and not isinstance(x, bool)]
    if not valid_ints:
        return None
    largest = valid_ints[0]
    for val in valid_ints:
        if val > largest:
            largest = val
    return largest

if __name__ == '__main__':
    scores = (95, 87.5, "100", 92, True, 88, -5, 105)
    result = find_largest_valid_int(scores)
    print(result)