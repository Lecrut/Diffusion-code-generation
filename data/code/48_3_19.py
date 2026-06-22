def get_largest_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 42, 'c': 7, 'd': 25}
    result = get_largest_value(sample_data)
    print(result)