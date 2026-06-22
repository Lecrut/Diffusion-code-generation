def find_largest_data_point(values):
    if not values:
        return None
    return max(values)

if __name__ == '__main__':
    sample_data = [15, 42, 8, 99, 3, 56]
    result = find_largest_data_point(sample_data)
    print(result)