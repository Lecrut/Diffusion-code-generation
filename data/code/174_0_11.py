def merge_dictionaries(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both arguments must be dictionaries.")
    return {**dict1, **dict2}

if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2}
    dict_b = {'b': 3, 'c': 4}
    merged_dict = merge_dictionaries(dict_a, dict_b)
    print(merged_dict)