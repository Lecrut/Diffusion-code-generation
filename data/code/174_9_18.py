def dict_intersection(dict1, dict2):
    return {key: value for key, value in dict1.items() if key in dict2 and dict2[key] == value}

if __name__ == '__main__':
    sample_dict1 = {'a': 1, 'b': 2, 'c': 3}
    sample_dict2 = {'b': 2, 'c': 4, 'd': 5}
    print(dict_intersection(sample_dict1, sample_dict2))