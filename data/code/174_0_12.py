def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

if __name__ == '__main__':
    first_dict = {'a': 1, 'b': 2}
    second_dict = {'b': 3, 'c': 4}
    result_dict = merge_dictionaries(first_dict, second_dict)
    print(result_dict)