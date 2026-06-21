def compare_dicts(dict1, dict2):
    keys_diff = set(dict1) ^ set(dict2)
    values_diff = {key: (dict1[key], dict2[key]) for key in set(dict1) & set(dict2) if dict1[key] != dict2[key]}
    return keys_diff, values_diff

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    keys_diff, values_diff = compare_dicts(sample_dict1, sample_dict2)
    print("Keys present in one but not the other:", keys_diff)
    print("Values that differ for common keys:", values_diff)