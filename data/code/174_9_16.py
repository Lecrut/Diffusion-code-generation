def intersect_dicts(dict1, dict2):
    return {key: value for key, value in dict1.items() if key in dict2 and dict2[key] == value}

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'd': 4}
    print(intersect_dicts(sample_dict1, sample_dict2))