def compare_dicts(dict1, dict2):
    result = {}
    for key in set(dict1) | set(dict2):
        if key not in dict1:
            result[key] = ('missing', dict2[key])
        elif key not in dict2:
            result[key] = (dict1[key], 'missing')
        else:
            if dict1[key] != dict2[key]:
                result[key] = (dict1[key], dict2[key])
    return result

if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2, 'c': 3}
    dict_b = {'b': 2, 'c': 4, 'd': 5}
    print(compare_dicts(dict_a, dict_b))