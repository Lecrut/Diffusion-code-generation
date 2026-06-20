def deep_equal(a, b):
    if type(a) != type(b):
        return False
    if isinstance(a, dict):
        if len(a) != len(b):
            return False
        for key in a:
            if key not in b or not deep_equal(a[key], b[key]):
                return False
        return True
    elif isinstance(a, list):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not deep_equal(a[i], b[i]):
                return False
        return True
    else:
        return a == b

if __name__ == '__main__':
    print(deep_equal({'a': 1, 'b': [2, 3]}, {'a': 1, 'b': [2, 3]}))
    print(deep_equal([1, 2, {'c': 4}], [1, 2, {'c': 4}]))
    print(deep_equal({'a': 1}, {'a': 2}))
    print(deep_equal([1, 2], [1, 3]))