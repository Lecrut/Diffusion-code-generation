def find_max_value(data):
    return max(data.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 50, 'c': 30}
    result = find_max_value(sample_dict)
    print(result)