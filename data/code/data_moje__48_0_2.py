def find_largest_data_point(values):
    if not values:
        raise ValueError("The list cannot be empty")
    return max(values)

if __name__ == '__main__':
    sample_data = [3.5, 12, 45.2, 8.9, 100, 55.1, 0.001]
    result = find_largest_data_point(sample_data)
    print(result)