def find_largest_data_point(data):
    if not data:
        return None
    return max(data)

if __name__ == '__main__':
    sample_data = [10, 3, 7, 1, 9, 4, 20, 15]
    result = find_largest_data_point(sample_data)
    print(result)