def find_common_pairs(dict1, dict2):
    common_items = {}
    for key, value in dict1.items():
        if key in dict2:
            if dict2[key] == value:
                common_items[key] = value
    return common_items
if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict_b = {'c': 3, 'd': 4, 'e': 5, 'f': 6}
    result = find_common_pairs(dict_a, dict_b)
    print(result)