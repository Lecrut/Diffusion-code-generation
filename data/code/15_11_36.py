def are_strictly_equal(a, b):
    if a is None or b is None:
        return a is b
    return a == b
if __name__ == '__main__':
    print(are_strictly_equal(None, None))
    print(are_strictly_equal(None, 0))
    print(are_strictly_equal(1, 1))
    print(are_strictly_equal(1, 2))
    print(are_strictly_equal('a', 'a'))
    print(are_strictly_equal('a', 'b'))