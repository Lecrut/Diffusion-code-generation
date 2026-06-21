def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

if __name__ == '__main__':
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    merged_dict = merge_dictionaries(d1, d2)
    print(merged_dict)