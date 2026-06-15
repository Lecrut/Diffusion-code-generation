def find_common_keys_from_dict1(dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())
    result = {}
    for key in common_keys:
        result[key] = dict1[key]
    return result
if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict_b = {'c': 30, 'd': 40, 'e': 50, 'f': 60}
    result1 = find_common_keys_from_dict1(dict_a, dict_b)
    print(result1)
    dict_x = {'apple': 100, 'banana': 200, 'cherry': 300}
    dict_y = {'banana': 200, 'date': 400, 'elderberry': 500}
    result2 = find_common_keys_from_dict1(dict_x, dict_y)
    print(result2)