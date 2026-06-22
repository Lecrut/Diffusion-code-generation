def find_largest_data_point(values):
    return max(values) if values else None

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = find_largest_data_point(sample_data)
    print(result)