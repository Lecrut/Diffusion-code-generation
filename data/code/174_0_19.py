def merge_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError('Both arguments must be dictionaries.')
    return {**dict1, **dict2}
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2}
    sample_dict2 = {'b': 3, 'c': 4}
    merged_dict = merge_dicts(sample_dict1, sample_dict2)
    print(merged_dict)