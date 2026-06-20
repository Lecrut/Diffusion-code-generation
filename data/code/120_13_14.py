def deep_equal(a, b):
    if a is b:
        return True
    if isinstance(a, dict) and isinstance(b, dict):
        if len(a) != len(b):
            return False
        for key in a:
            if key not in b or not deep_equal(a[key], b[key]):
                return False
        return True
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for item1, item2 in zip(a, b):
            if not deep_equal(item1, item2):
                return False
        return True
    if isinstance(a, tuple) and isinstance(b, tuple):
        if len(a) != len(b):
            return False
        for item1, item2 in zip(a, b):
            if not deep_equal(item1, item2):
                return False
        return True
    if isinstance(a, set) and isinstance(b, set):
        if len(a) != len(b):
            return False
        for item in a:
            if item not in b or not deep_equal(item, b[item]):
                return False
        return True
    return a == b

if __name__ == '__main__':
    print(deep_equal({'a': 1, 'b': [2, 3]}, {'a': 1, 'b': [2, 3]}))
    print(deep_equal([1, 2, 3], (1, 2, 3)))
    print(deep_equal({1, 2, 3}, {3, 2, 1}))
    print(deep_equal('hello', 'hello'))
    print(deep_equal(42, 42))
    print(deep_equal(None, None))