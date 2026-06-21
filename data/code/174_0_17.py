def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2}
    sample_dict2 = {'b': 3, 'c': 4}
    result_dict = merge_dictionaries(sample_dict1, sample_dict2)
    print(result_dict)