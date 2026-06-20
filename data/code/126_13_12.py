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
    sample_a = {'a': 1, 'b': {'c': 2}}
    sample_b = {'a': 1, 'b': {'c': 2}}
    print(dict_equal(sample_a, sample_b))
    
    sample_c = {'x': [4, 5], 'y': {'z': {'w': 6}}}
    sample_d = {'x': [4, 5], 'y': {'z': {'w': 6}}}
    print(dict_equal(sample_c, sample_d))