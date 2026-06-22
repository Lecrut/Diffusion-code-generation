def are_strictly_equal(value1, value2):
    if value1 is None and value2 is None:
        return True
    elif value1 is None or value2 is None:
        return False
    else:
        return value1 == value2
if __name__ == '__main__':
    a = 42
    b = 42
    c = None
    d = None
    e = []
    print(are_strictly_equal(a, b))
    print(are_strictly_equal(c, d))
    print(are_strictly_equal(a, c))
    print(are_strictly_equal(e, []))