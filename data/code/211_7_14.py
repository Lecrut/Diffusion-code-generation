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
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 2, 'c': 4, 'd': 5}
    print(compare_dicts(dict1, dict2))