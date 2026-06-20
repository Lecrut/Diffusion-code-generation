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
    sample4 = {'m': 5, 'n': {'o': [4, 5, 6]}}
    sample5 = {'m': 5, 'n': {'o': [4, 5, 6]}}
    print(dict_equal(sample4, sample5))
    sample6 = {'m': 5, 'n': {'o': [4, 5, 7]}}
    print(dict_equal(sample4, sample6))