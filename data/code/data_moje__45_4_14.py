def find_minimum(values):
    if not values:
        raise ValueError("The list of values cannot be empty")
    min_val = values[0]
    for val in values[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_data = [34, 12, 99, 2, 55, 1, 88, 40]
    result = find_minimum(sample_data)
    print(result)