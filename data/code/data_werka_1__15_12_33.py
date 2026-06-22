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
    value3 = None
    value4 = None
    value5 = 'hello'
    value6 = 'world'
    print(are_strictly_equal(value1, value2))
    print(are_strictly_equal(value3, value4))
    print(are_strictly_equal(value1, value3))
    print(are_strictly_equal(value5, value6))