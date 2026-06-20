def deep_equal(a, b):
    if a is b:
        return True
    if type(a) != type(b):
        return False
    if isinstance(a, (int, float, str, bool)):
        return a == b
    if isinstance(a, list):
        if len(a) != len(b):
            return False
        for item_a, item_b in zip(a, b):
            if not deep_equal(item_a, item_b):
                return False
        return True
    if isinstance(a, dict):
        if len(a) != len(b):
            return False
        for key, value in a.items():
            if key not in b or not deep_equal(value, b[key]):
                return False
        return True
    raise ValueError('Unsupported data type')
if __name__ == '__main__':
    print(deep_equal([1, 2, [3]], [1, 2, [3]]))
    print(deep_equal({'a': 1}, {'a': 1}))
    print(deep_equal(1, 1))
    print(deep_equal(None, None))
    print(deep_equal([1, 2], [1]))