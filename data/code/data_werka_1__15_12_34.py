def are_strictly_equal(a, b):
    if a is None or b is None:
        return a is b
    else:
        return a == b
if __name__ == '__main__':
    print(are_strictly_equal(None, None))
    print(are_strictly_equal(None, 0))
    print(are_strictly_equal(0, 0))
    print(are_strictly_equal([], []))
    print(are_strictly_equal('a', 'a'))