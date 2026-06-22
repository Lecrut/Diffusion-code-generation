def get_largest_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 50, 'c': 25, 'd': 75}
    result = get_largest_value(sample_dict)
    print(result)