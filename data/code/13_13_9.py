def get_value(data, key, default=None):
    return data.get(key, default)

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    result = get_value(sample_dict, 'b', 99)
    print(result)
    result_missing = get_value(sample_dict, 'z', 0)
    print(result_missing)