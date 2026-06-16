def has_common_key(dict1: dict, dict2: dict) -> bool:
    return set(dict1.keys()) & set(dict2.keys()) != set()
if __name__ == '__main__':
    d_a = {'x': 10, 'y': 20}
    d_b = {'p': 30, 'q': 40}
    print(has_common_key(d_a, d_b))
    d_c = {'a': 5, 'b': 6}
    d_d = {'c': 7, 'd': 8}
    print(has_common_key(d_c, d_d))
    e1 = {'key': 'val'}
    e2 = {'key': 'other'}
    print(has_common_key(e1, e2))