def are_equal(a, b):
    if type(a) is type(b):
        return a == b
    try:
        return a == b
    except TypeError:
        return False
if __name__ == '__main__':
    print(are_equal(10, 10))
    print(are_equal("hello", "hello"))
    print(are_equal(10, "10"))
    print(are_equal([1, 2], [1, 2]))
    print(are_equal(3.14, 3.14))
    print(are_equal(10, 20))
    print(are_equal(None, None))
    print(are_equal(5, "5"))
    print(are_equal([1, 2], [2, 1]))