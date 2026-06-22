def find_largest_data_point(values):
    if not values:
        raise ValueError("The list of values cannot be empty")
    return max(values)

if __name__ == '__main__':
    sample_data = [15, 42, 7, 99, 23, 56, 12]
    result = find_largest_data_point(sample_data)
    print(result)