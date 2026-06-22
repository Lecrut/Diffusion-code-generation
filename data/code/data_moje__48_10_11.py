def find_largest_value(values):
    if not values:
        raise ValueError("The list cannot be empty")
    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    sample_values = [12, 45, 2, 99, 34, 67, 5, 88, 1, 100]
    result = find_largest_value(sample_values)
    print(result)