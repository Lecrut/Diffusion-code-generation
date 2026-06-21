def validate_dictionary(dictionary):
    if not isinstance(dictionary, dict):
        raise ValueError('Input must be a dictionary')

def compare_dictionaries(dict1, dict2):
    validate_dictionary(dict1)
    validate_dictionary(dict2)
    return all((key in dict2 and dict1[key] == dict2[key] for key in dict1))
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'a': 1, 'b': 2, 'c': 3}
    print(compare_dictionaries(sample_dict1, sample_dict2))
    sample_dict3 = {'a': 1, 'b': 2, 'd': 4}
    print(compare_dictionaries(sample_dict1, sample_dict3))