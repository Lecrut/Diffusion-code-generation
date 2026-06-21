def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

if __name__ == '__main__':
    dict_a = {'x': 10, 'y': 20}
    dict_b = {'y': 30, 'z': 40}
    merged_dict = merge_dictionaries(dict_a, dict_b)
    print(merged_dict)