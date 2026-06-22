def compare_dictionaries(dict1, dict2):
    return {key: value for key, value in dict1.items() if key in dict2 and dict1[key] == dict2[key]}

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'a': 1, 'c': 4, 'd': 5}
    result = compare_dictionaries(sample_dict1, sample_dict2)
    print(result)