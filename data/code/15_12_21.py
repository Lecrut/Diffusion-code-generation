def are_strictly_equal(value1, value2):
    if value1 is None or value2 is None:
        return value1 is value2
    else:
        return value1 == value2
if __name__ == '__main__':
    a = 42
    b = 42
    c = None
    d = None
    e = [1, 2, 3]
    f = [1, 2, 3]
    print(are_strictly_equal(a, b))
    print(are_strictly_equal(c, d))
    print(are_strictly_equal(a, c))
    print(are_strictly_equal(e, f))