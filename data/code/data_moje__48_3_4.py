def find_largest_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 25, 'c': 7, 'd': 30}
    result = find_largest_value(sample_dict)
    print(result)