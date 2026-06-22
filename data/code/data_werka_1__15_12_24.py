def are_strictly_equal(a, b):
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False
    else:
        return a == b

if __name__ == '__main__':
    value1 = 42
    value2 = 42
    result = are_strictly_equal(value1, value2)
    print(result)

    value3 = None
    value4 = None
    result = are_strictly_equal(value3, value4)
    print(result)

    value5 = None
    value6 = 0
    result = are_strictly_equal(value5, value6)
    print(result)

    value7 = []
    value8 = []
    result = are_strictly_equal(value7, value8)
    print(result)