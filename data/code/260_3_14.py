def compare_dictionaries(dict1, dict2):
    common_pairs = {key: value for key, value in dict1.items() if key in dict2 and dict2[key] == value}
    return common_pairs
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    sample_dict2 = {'b': 2, 'd': 4, 'e': 5, 'f': 6}
    result = compare_dictionaries(sample_dict1, sample_dict2)
    print(result)