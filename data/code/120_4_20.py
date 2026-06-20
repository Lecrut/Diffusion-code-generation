def are_equal(var1, var2):
    return var1 == var2
if __name__ == '__main__':
    print(are_equal(5, 5))
    print(are_equal('hello', 'hello'))
    print(are_equal([1, 2, 3], [1, 2, 3]))
    print(are_equal({'a': 1}, {'a': 1}))
    print(are_equal(None, None))
    print(are_equal(True, True))
    print(are_equal(False, False))
    print(are_equal(5, '5'))
    print(are_equal([1, 2], [1, 3]))
    print(are_equal({'a': 1}, {'b': 1}))