def find_max_value(data_dict):
    return max(data_dict.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 25, 'c': 5, 'd': 30}
    result = find_max_value(sample_dict)
    print(result)