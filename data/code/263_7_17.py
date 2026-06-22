def merge_dictionaries(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both arguments must be dictionaries.")
    
    result = {}
    for key in set(dict1).intersection(set(dict2)):
        result[key] = dict1[key] + dict2[key]
    return result

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 3, 'c': 4, 'd': 5}
    print(merge_dictionaries(sample_dict1, sample_dict2))