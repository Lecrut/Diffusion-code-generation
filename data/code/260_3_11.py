def intersect_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Both arguments must be dictionaries")
    
    return {key: value for key, value in dict1.items() if key in dict2 and dict1[key] == dict2[key]}

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    result = intersect_dicts(sample_dict1, sample_dict2)
    print(f"Intersection: {result}")