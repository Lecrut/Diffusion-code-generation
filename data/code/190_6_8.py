def key_in_dict_list(key, dict_list):
    keys_set = set(d.keys() for d in dict_list)
    return key in keys_set

if __name__ == '__main__':
    sample_key = 'example_key'
    sample_dicts = [{'a': 1}, {'b': 2}, {'example_key': 3}]
    print(key_in_dict_list(sample_key, sample_dicts))