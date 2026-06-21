def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
if __name__ == '__main__':
    dict_a = {'a': 5, 'b': 3}
    dict_b = {'b': 2, 'c': 4}
    merged_dict = merge_dictionaries(dict_a, dict_b)
    print(merged_dict)