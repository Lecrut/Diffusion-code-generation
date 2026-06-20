def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    print(are_values_equal(1, 1))
    print(are_values_equal('a', 'a'))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal(3.14, 3.14))
    print(are_values_equal(None, None))
    print(are_values_equal(True, True))
    print(are_values_equal(False, False))
    print(are_values_equal({}, {}))
    print(are_values_equal((1, 2), (1, 2)))
    print(are_values_equal('hello', 'world'))