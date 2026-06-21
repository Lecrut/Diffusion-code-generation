def validate_dict(input_dict):
    if not isinstance(input_dict, dict):
        raise TypeError('Input must be a dictionary.')
    for key, value in input_dict.items():
        if not isinstance(key, str) or not isinstance(value, (int, float)):
            raise ValueError('Dictionary keys must be strings and values must be integers or floats.')

def compare_dicts(dict1, dict2):
    validate_dict(dict1)
    validate_dict(dict2)
    return all((key in dict2 and dict1[key] == dict2[key] for key in dict1))
if __name__ == '__main__':
    sample_dict1 = {'apple': 3.5, 'banana': 0.75}
    sample_dict2 = {'apple': 3.5, 'banana': 0.75}
    result = compare_dicts(sample_dict1, sample_dict2)
    print(result)