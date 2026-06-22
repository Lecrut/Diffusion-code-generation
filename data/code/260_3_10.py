def compare_dicts(dict1, dict2):
    common_pairs = {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}
    return common_pairs
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    result = compare_dicts(sample_dict1, sample_dict2)
    print(result)