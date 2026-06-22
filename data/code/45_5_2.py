def get_minimum(values):
    if not isinstance(values, list):
        raise TypeError("Input must be a list")
    if len(values) == 0:
        raise ValueError("List must not be empty")
    min_val = values[0]
    for num in values[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7]
    result = get_minimum(sample_list)
    print(result)