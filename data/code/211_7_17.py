def compare_dicts(dict1, dict2):
    def get_only_in_dict(source, target):
        return {k: v for k, v in source.items() if k not in target}

    def get_diff_values(dict_a, dict_b):
        common_keys = set(dict_a) & set(dict_b)
        return {k: (dict_a[k], dict_b[k]) for k in common_keys if dict_a[k] != dict_b[k]}

    only_in_dict1 = get_only_in_dict(dict1, dict2)
    only_in_dict2 = get_only_in_dict(dict2, dict1)
    diff_values = get_diff_values(dict1, dict2)

    return only_in_dict1, only_in_dict2, diff_values

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    result = compare_dicts(sample_dict1, sample_dict2)
    print(result)