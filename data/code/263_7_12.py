def merge_dictionaries(dict1, dict2):
    result = {}
    for key in set(dict1) & set(dict2):
        result[key] = dict1[key] + dict2[key]
    return result

if __name__ == '__main__':
    sample_dict1 = {'x': 5, 'y': 10, 'z': 15}
    sample_dict2 = {'y': 3, 'z': 7, 'w': 9}
    print(merge_dictionaries(sample_dict1, sample_dict2))