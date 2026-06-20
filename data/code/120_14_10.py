def fast_compare(a, b):
    if a is b:
        return True
    if type(a) != type(b):
        return False
    if isinstance(a, (int, float, str)):
        return a == b
    if isinstance(a, list):
        return len(a) == len(b) and all(fast_compare(x, y) for x, y in zip(a, b))
    if isinstance(a, dict):
        return len(a) == len(b) and all(k in b and fast_compare(v, b[k]) for k, v in a.items())
    raise TypeError("Unsupported type for comparison")

if __name__ == '__main__':
    print(fast_compare(10, 10))
    print(fast_compare('hello', 'hello'))
    print(fast_compare([1, 2], [1, 2]))
    print(fast_compare({'a': 1}, {'a': 1}))
    print(fast_compare(None, None))
    try:
        print(fast_compare(10, '10'))
    except TypeError as e:
        print(e)