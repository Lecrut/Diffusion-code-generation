def merge_dictionaries(dict1, dict2):
    result = {}
    for key in set(dict1) | set(dict2):
        if key in dict1 and key in dict2:
            result[key] = dict1[key] + dict2[key]
        elif key in dict1:
            result[key] = dict1[key]
        else:
            result[key] = dict2[key]
    return result

if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2, 'c': 3}
    dict_b = {'b': 3, 'c': 4, 'd': 5}
    merged_dict = merge_dictionaries(dict_a, dict_b)
    print(merged_dict)