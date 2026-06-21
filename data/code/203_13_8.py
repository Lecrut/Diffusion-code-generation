def compare_dictionaries(dict1, dict2):
    for key, value in dict1.items():
        if key not in dict2 or dict2[key] != value:
            return False
    return True
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'a': 1, 'b': 2, 'c': 3}
    result = compare_dictionaries(sample_dict1, sample_dict2)
    print(result)