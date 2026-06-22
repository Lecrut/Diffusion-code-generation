def get_value_with_default(dictionary, key, default):
    return dictionary.get(key, default)

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    result = get_value_with_default(sample_dict, 'b', 0)
    print(result)
    result_missing = get_value_with_default(sample_dict, 'z', 99)
    print(result_missing)