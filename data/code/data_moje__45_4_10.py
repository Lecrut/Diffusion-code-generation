def find_minimum(values):
    if not values:
        raise ValueError("List cannot be empty")
    min_val = values[0]
    for val in values[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_data = [53, 12, 99, 4, 78, 23, 1, 45, 88, 10]
    result = find_minimum(sample_data)
    print(result)