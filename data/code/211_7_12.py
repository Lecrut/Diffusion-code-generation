def compare_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both arguments must be dictionaries")

    only_in_dict1 = {k: v for k, v in dict1.items() if k not in dict2}
    only_in_dict2 = {k: v for k, v in dict2.items() if k not in dict1}
    diff_values = {
        k: (dict1[k], dict2[k]) 
        for k in set(dict1) & set(dict2) 
        if dict1[k] != dict2[k]
    }
    
    return only_in_dict1, only_in_dict2, diff_values

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    result = compare_dicts(sample_dict1, sample_dict2)
    print(result)