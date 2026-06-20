def are_identical(a, b):
    return a == b
if __name__ == '__main__':
    print(are_identical(1, 1))
    print(are_identical('hello', 'hello'))
    print(are_identical([1, 2, 3], [1, 2, 3]))
    print(are_identical(None, None))
    print(are_identical(True, True))
    print(are_identical(False, False))
    print(are_identical(1, '1'))
    print(are_identical([1, 2], [1, 2, 3]))