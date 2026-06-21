def compare_dictionaries(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both inputs must be dictionaries.")
    
    return dict1 == dict2

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2}
    sample_dict2 = {'a': 1, 'b': 2}
    comparison_result = compare_dictionaries(sample_dict1, sample_dict2)
    print(comparison_result)