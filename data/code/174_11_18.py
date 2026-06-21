def merge_dictionaries(dict1, dict2):
    result = {}
    all_keys = set(dict1.keys()).union(set(dict2.keys()))
    for key in all_keys:
        value1 = dict1.get(key, 0)
        value2 = dict2.get(key, 0)
        result[key] = value1 + value2
    return result

if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 3, 'c': 5}
    dict_b = {'b': 4, 'c': 6, 'd': 7}
    merged_dict = merge_dictionaries(dict_a, dict_b)
    print(merged_dict)