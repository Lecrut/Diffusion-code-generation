def are_dicts_equal_ignore_order(dict1, dict2):
    return set(dict1.items()) == set(dict2.items())
if __name__ == '__main__':
    dict_a = {'a': 1, 'b': 2}
    dict_b = {'b': 2, 'a': 1}
    dict_c = {'a': 1, 'c': 3}
    print(are_dicts_equal_ignore_order(dict_a, dict_b))
    print(are_dicts_equal_ignore_order(dict_a, dict_c))