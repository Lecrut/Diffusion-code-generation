def find_highest_value(data_dict):
    return max(data_dict.values(), default=None)

if __name__ == '__main__':
    sample_data = {'a': 3, 'b': 5, 'c': 1, 'd': 8}
    result = find_highest_value(sample_data)
    print(result)