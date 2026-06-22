def find_minimum(values):
    if not values:
        raise ValueError("Cannot find minimum of an empty list")
    min_val = values[0]
    for i in range(1, len(values)):
        if values[i] < min_val:
            min_val = values[i]
    return min_val

if __name__ == '__main__':
    sample_data = [34, 12, 8, 99, 2, 45, 1, 67, 23, 5]
    result = find_minimum(sample_data)
    print(result)