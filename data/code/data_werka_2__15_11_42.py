def are_strictly_equal(a, b):
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False
    else:
        return a is b and a == b
if __name__ == '__main__':
    print(are_strictly_equal(None, None))
    print(are_strictly_equal(None, 0))
    print(are_strictly_equal(10, 10))
    print(are_strictly_equal('hello', 'hello'))
    print(are_strictly_equal([], []))
    print(are_strictly_equal({}, {}))