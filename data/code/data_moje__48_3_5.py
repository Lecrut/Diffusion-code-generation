def find_largest_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 45, 'c': 23, 'd': 67, 'e': 5}
    result = find_largest_value(sample_dict)
    print(result)