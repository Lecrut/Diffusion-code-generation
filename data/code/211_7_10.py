def compare_dicts(dict1, dict2):
    keys_diff = set(dict1.keys()) ^ set(dict2.keys())
    values_diff = {k: (dict1[k], dict2[k]) for k in dict1 if k in dict2 and dict1[k] != dict2[k]}
    return {'keys_diff': keys_diff, 'values_diff': values_diff}

if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2, 'c': 3}
    dict_b = {'b': 2, 'c': 4, 'd': 5}
    result = compare_dicts(dict_a, dict_b)
    print(result)