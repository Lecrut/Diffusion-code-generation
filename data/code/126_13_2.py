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
    sample1 = {'x': 42, 'y': {'z': [1, 2, 3]}}
    sample2 = {'x': 42, 'y': {'z': [1, 2, 3]}}
    print(dict_equal(sample1, sample2))
    
    sample3 = {'x': 42, 'y': {'z': [1, 2, 4]}}
    print(dict_equal(sample1, sample3))