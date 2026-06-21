def key_exists(key, dict_list):
    keys_set = set((item.keys() for item in dict_list))
    return key in keys_set
if __name__ == '__main__':
    sample_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    print(key_exists('b', sample_dicts))
    print(key_exists('d', sample_dicts))