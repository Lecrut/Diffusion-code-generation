def find_largest_data_point(data):
    return max(data)

if __name__ == '__main__':
    sample_data = [10, 45, 3, 92, 17, 50, 8]
    result = find_largest_data_point(sample_data)
    print(result)