def sum_common_values(dict1, dict2):
    common_keys = set(dict1) & set(dict2)
    result = {}
    for key in common_keys:
        result[key] = dict1[key] + dict2[key]
    return result

if __name__ == '__main__':
    dict_a = {'x': 5, 'y': 10, 'z': 15}
    dict_b = {'y': 3, 'z': 8, 'w': 20}
    summed_dict = sum_common_values(dict_a, dict_b)
    print(summed_dict)