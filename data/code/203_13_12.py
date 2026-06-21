def compare_dictionaries(dict1, dict2):
    return all(key in dict2 and dict1[key] == dict2[key] for key in dict1)

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'a': 1, 'b': 2, 'c': 3}
    comparison_result = compare_dictionaries(sample_dict1, sample_dict2)
    print(comparison_result)