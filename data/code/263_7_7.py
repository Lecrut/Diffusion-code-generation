def validate_dictionaries(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both inputs must be dictionaries.")
    return dict1, dict2

def merge_dictionaries(dict1, dict2):
    dict1, dict2 = validate_dictionaries(dict1, dict2)
    result = {}
    common_keys = set(dict1) & set(dict2)
    for key in common_keys:
        result[key] = dict1[key] + dict2[key]
    return result

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 3, 'c': 4, 'd': 5}
    print(merge_dictionaries(sample_dict1, sample_dict2))