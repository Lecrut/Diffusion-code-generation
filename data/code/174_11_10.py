def merge_dictionaries(dict1, dict2):
    merged_dict = {}
    for key in set(dict1) | set(dict2):
        merged_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)
    return merged_dict
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 3, 'c': 4, 'd': 5}
    result = merge_dictionaries(sample_dict1, sample_dict2)
    print(result)