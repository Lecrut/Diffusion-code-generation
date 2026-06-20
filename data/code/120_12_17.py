def are_identical(a, b):
    return a is b
if __name__ == '__main__':
    print(are_identical(1, 1))
    print(are_identical('hello', 'hello'))
    print(are_identical(None, None))
    print(are_identical([1, 2], [1, 2]))