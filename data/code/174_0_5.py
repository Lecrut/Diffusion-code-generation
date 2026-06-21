def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

if __name__ == '__main__':
    dict_a = {"a": 1, "b": 2}
    dict_b = {"b": 3, "c": 4}
    merged_dict = merge_dictionaries(dict_a, dict_b)
    print(merged_dict)