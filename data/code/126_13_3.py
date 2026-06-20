def dict_equal(d1, d2):
    if d1 is d2:
        return True
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        return False
    if len(d1) != len(d2):
        return False
    for k in d1:
        if k not in d2 or not dict_equal(d1[k], d2[k]):
            return False
    return True
if __name__ == '__main__':
    sample1 = {'a': 1, 'b': {'c': 2}}
    sample2 = {'a': 1, 'b': {'c': 2}}
    print(dict_equal(sample1, sample2))
    sample3 = {'a': 1, 'b': {'c': 3}}
    print(dict_equal(sample1, sample3))