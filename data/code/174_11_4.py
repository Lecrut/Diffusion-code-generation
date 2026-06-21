def merge_dictionaries(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        if key in dict2:
            result[key] = value + dict2[key]
        else:
            result[key] = value
    for key, value in dict2.items():
        if key not in result:
            result[key] = value
    return result

if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    merged_dict = merge_dictionaries(dict1, dict2)
    print(merged_dict)