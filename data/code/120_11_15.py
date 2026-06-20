def are_equal(a, b):
    if type(a) != type(b):
        return False
    return a == b

if __name__ == '__main__':
    print(are_equal(1, 2))
    print(are_equal('hello', 'hello'))
    print(are_equal([1, 2], [1, 2]))
    print(are_equal({'a': 1}, {'a': 1}))
    print(are_equal((1, 2), (1, 2)))
    print(are_equal(True, True))
    print(are_equal(False, False))
    print(are_equal(None, None))