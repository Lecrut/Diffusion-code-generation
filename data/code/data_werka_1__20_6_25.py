def deep_equal(a, b):
    if type(a) != type(b):
        return False
    if isinstance(a, dict):
        return all((deep_equal(a[k], b[k]) for k in a.keys() if k in b)) and all((k in a for k in b))
    elif isinstance(a, list):
        return len(a) == len(b) and all((deep_equal(x, y) for x, y in zip(a, b)))
    else:
        return a == b
if __name__ == '__main__':
    sample1 = {'a': [1, 2, {'b': 3}], 'c': (4, 5)}
    sample2 = {'a': [1, 2, {'b': 3}], 'c': (4, 5)}
    sample3 = {'a': [1, 2, {'b': 4}], 'c': (4, 5)}
    print(deep_equal(sample1, sample2))
    print(deep_equal(sample1, sample3))