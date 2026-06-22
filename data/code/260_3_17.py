def validate_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both inputs must be dictionaries")

def intersect_dicts(dict1, dict2):
    return {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    
    validate_dicts(sample_dict1, sample_dict2)
    result = intersect_dicts(sample_dict1, sample_dict2)
    print(f"Intersecting dictionary: {result}")