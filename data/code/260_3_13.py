def validate_inputs(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both inputs must be dictionaries.")
    return dict1, dict2

def intersect_dictionaries(dict1, dict2):
    return {key: value for key, value in dict1.items() if key in dict2 and dict2[key] == value}

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    validated_dicts = validate_inputs(sample_dict1, sample_dict2)
    result = intersect_dictionaries(*validated_dicts)
    print(f"Intersection of dictionaries: {result}")