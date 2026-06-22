def get_largest_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 50, 'c': 20, 'd': 30}
    result = get_largest_value(sample_data)
    print(result)