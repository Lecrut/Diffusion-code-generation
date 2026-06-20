def dicts_are_equal(d1, d2):
    if d1 is d2:
        return True
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        return False
    if len(d1) != len(d2):
        return False
    for key in d1:
        if key not in d2 or not dicts_are_equal(d1[key], d2[key]):
            return False
    return True

if __name__ == '__main__':
    print(dicts_are_equal({'a': 1, 'b': {'c': 2}}, {'a': 1, 'b': {'c': 2}}))
    print(dicts_are_equal({'a': 1, 'b': {'c': 3}}, {'a': 1, 'b': {'c': 2}}))