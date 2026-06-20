def are_equal(a, b):
    if a == b:
        return True
    elif isinstance(a, dict) and isinstance(b, dict):
        return all(are_equal(k, v) for k, v in a.items() if k in b) and len(a) == len(b)
    elif isinstance(a, list) and isinstance(b, list):
        return all(are_equal(x, y) for x, y in zip(a, b)) and len(a) == len(b)
    else:
        return False

if __name__ == '__main__':
    print(are_equal({'a': 1, 'b': [2, 3]}, {'a': 1, 'b': [2, 3]}))
    print(are_equal([1, 2, 3], [1, 2, 3]))
    print(are_equal((1, 2), (1, 2)))
    print(are_equal('hello', 'hello'))
    print(are_equal(None, None))
    print(are_equal(True, True))
    print(are_equal(False, False))
    print(are_equal(1, 1.0))
    print(are_equal(1, 2))