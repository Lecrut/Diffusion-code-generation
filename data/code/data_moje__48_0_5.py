def find_largest_data_point(values):
    if not values:
        return None
    return max(values)

if __name__ == '__main__':
    sample_data = [3, 5, 1, 9, 2, 8, 4]
    result = find_largest_data_point(sample_data)
    print(result)