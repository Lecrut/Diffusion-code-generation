def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}
if __name__ == '__main__':
    first_dict = {'a': 1, 'b': 2}
    second_dict = {'b': 3, 'c': 4}
    merged_dict = merge_dictionaries(first_dict, second_dict)
    print(merged_dict)