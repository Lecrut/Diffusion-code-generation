def merge_dictionaries(dict1, dict2):
    result = {}
    all_keys = set(dict1.keys()).union(dict2.keys())
    for key in all_keys:
        result[key] = (dict1.get(key, 0) + dict2.get(key, 0))
    return result

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 3, 'c': 4, 'd': 5}
    merged_dict = merge_dictionaries(sample_dict1, sample_dict2)
    print(merged_dict)