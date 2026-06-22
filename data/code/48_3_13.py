def find_largest_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 45, 'c': 30, 'd': 5}
    result = find_largest_value(sample_data)
    print(result)