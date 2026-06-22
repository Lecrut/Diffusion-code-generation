def find_largest_data_point(values):
    if not values:
        raise ValueError("List must not be empty")
    return max(values)

if __name__ == '__main__':
    sample_values = [10, 45, 3, 89, 22, 67, 5]
    result = find_largest_data_point(sample_values)
    print(result)