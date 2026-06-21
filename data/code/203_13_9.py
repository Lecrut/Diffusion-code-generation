def compare_dictionaries(dict1, dict2):
    if set(dict1.keys()) != set(dict2.keys()):
        return False
    for key in dict1:
        if dict1[key] != dict2[key]:
            return False
    return True
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2}
    sample_dict2 = {'a': 1, 'b': 2}
    print(compare_dictionaries(sample_dict1, sample_dict2))