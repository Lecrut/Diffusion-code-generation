def find_largest(values):
    if not values:
        raise ValueError("List cannot be empty")
    largest_value = values[0]
    for value in values[1:]:
        if value > largest_value:
            largest_value = value
    return largest_value

if __name__ == '__main__':
    sample_data = [15, 42, 7, 89, 23, 55, 12, 99, 34]
    result = find_largest(sample_data)
    print(result)