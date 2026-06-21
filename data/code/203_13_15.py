def validate_dict_input(d1, d2):
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise ValueError('Both inputs must be dictionaries.')
    if len(d1) == 0:
        raise ValueError('First dictionary is empty.')
    if len(d2) == 0:
        raise ValueError('Second dictionary is empty.')

def compare_dictionaries(dict1, dict2):
    try:
        validate_dict_input(dict1, dict2)
        return all((dict1.get(key) == dict2.get(key) for key in dict1.keys()))
    except ValueError as e:
        print(e)
        return False
if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'a': 1, 'b': 2, 'd': 4}
    result = compare_dictionaries(sample_dict1, sample_dict2)
    print(result)