def find_largest_data_point(data):
    return max(data)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_largest_data_point(sample_data)
    print(result)