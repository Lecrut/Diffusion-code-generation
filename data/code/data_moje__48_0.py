def find_largest_data_point(values):
    return max(values)

if __name__ == '__main__':
    sample_data = [3.14, 100, -50, 75.5, 42, 0, -99.9]
    result = find_largest_data_point(sample_data)
    print(result)