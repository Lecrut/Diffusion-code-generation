def find_common_pairs(dict1, dict2):
    common_items = {key: (dict1[key], dict2[key]) for key in dict1 if key in dict2}
    return dict(common_items)
if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict_b = {'c': 3, 'd': 4, 'e': 5, 'f': 6}
    result = find_common_pairs(dict_a, dict_b)
    print(result)