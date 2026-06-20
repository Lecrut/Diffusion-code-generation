def are_identical(a, b):
    return a == b

if __name__ == '__main__':
    print(are_identical(5, 5))
    print(are_identical("hello", "hello"))
    print(are_identical([1, 2], [1, 2]))
    print(are_identical(3.14, 3.14))
    print(are_identical(True, True))
    print(are_identical(None, None))