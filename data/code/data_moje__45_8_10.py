def find_minimum(values):
    if not values:
        raise ValueError("List must not be empty")
    min_val = values[0]
    for val in values[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 67, 43, 11]
    result = find_minimum(sample_list)
    print(result)