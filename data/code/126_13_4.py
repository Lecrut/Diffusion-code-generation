def dict_equal(d1, d2):
    if d1 is d2:
        return True
    if not (isinstance(d1, dict) and isinstance(d2, dict)):
        return False
    if len(d1) != len(d2):
        return False
    for k in d1:
        if k not in d2 or not dict_equal(d1[k], d2[k]):
            return False
    return True

if __name__ == '__main__':
    print(dict_equal({'a': 1, 'b': {'c': 2}}, {'a': 1, 'b': {'c': 2}}))
    print(dict_equal({'a': 1, 'b': {'c': 3}}, {'a': 1, 'b': {'c': 2}}))