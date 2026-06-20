def is_equal(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) < 1e-9
    elif isinstance(a, str) and isinstance(b, str):
        return a == b
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for item_a, item_b in zip(a, b):
            if not is_equal(item_a, item_b):
                return False
        return True
    elif isinstance(a, dict) and isinstance(b, dict):
        if len(a) != len(b):
            return False
        for key, value in a.items():
            if key not in b or not is_equal(value, b[key]):
                return False
        return True
    else:
        return a == b

if __name__ == '__main__':
    print(is_equal(10, 10))
    print(is_equal(10.0, 10))
    print(is_equal('hello', 'hello'))
    print(is_equal([1, 2], [1, 2]))
    print(is_equal({'a': 1}, {'a': 1}))
    print(is_equal(None, None))
    print(is_equal(10, '10'))