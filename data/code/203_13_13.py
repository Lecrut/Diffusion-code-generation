def compare_dictionaries(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError('Both arguments must be dictionaries.')
    return all((dict1.get(key, None) == dict2.get(key, None) for key in dict1))
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'a': 1, 'b': 2, 'c': 4}
    result = compare_dictionaries(sample_dict1, sample_dict2)
    print(result)