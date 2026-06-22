def find_largest_data_point(values):
    if not values:
        raise ValueError("The list is empty")
    return max(values)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_largest_data_point(sample_values)
    print(result)