def merge_dictionaries(dict1, dict2):
    merged = {}
    for key in set(dict1) | set(dict2):
        merged[key] = dict1.get(key, 0) + dict2.get(key, 0)
    return merged

if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 3, 'c': 5}
    dict_b = {'b': 4, 'c': 6, 'd': 8}
    result = merge_dictionaries(dict_a, dict_b)
    print(result)