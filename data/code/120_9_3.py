def are_equal(a, b):
    if type(a) != type(b):
        return False
    if a == b:
        return True
    return False
if __name__ == '__main__':
    print(are_equal(10, 10))
    print(are_equal("hello", "hello"))
    print(are_equal(10, 20))
    print(are_equal(3.14, 3.14))
    print(are_equal(10, 10.0))
    print(are_equal([1, 2], [1, 2]))
    print(are_equal([1, 2], [2, 1]))
    print(are_equal(True, True))
    print(are_equal(False, False))
    print(are_equal(1, "1"))
    print(are_equal(None, None))