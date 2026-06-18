def has_common_key(dict1: dict, dict2: dict) -> bool:
    return set(dict1.keys()).intersection(set(dict2.keys()))
if __name__ == '__main__':
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}
    result_1 = has_common_key(d1, d2)
    d3 = {'e': 5}
    d4 = {'f': 6, 'g': 7}
    result_2 = has_common_key(d3, d4)
    print(result_1 is False and result_2 is True)