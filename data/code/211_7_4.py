def compare_dicts(dict1, dict2):
    diff = {}
    for key in set(dict1) | set(dict2):
        if key not in dict1:
            diff[key] = (None, dict2[key])
        elif key not in dict2:
            diff[key] = (dict1[key], None)
        else:
            if dict1[key] != dict2[key]:
                diff[key] = (dict1[key], dict2[key])
    return diff

if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2, 'c': 3}
    dict_b = {'b': 2, 'c': 4, 'd': 5}
    print(compare_dicts(dict_a, dict_b))