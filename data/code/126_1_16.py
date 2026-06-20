def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    print(are_values_equal(10, 10))
    print(are_values_equal("hello", "hello"))
    print(are_values_equal(3.14, 3.14))
    print(are_values_equal(True, True))
    print(are_values_equal(False, False))
    print(are_values_equal(None, None))
    print(are_values_equal([1, 2], [1, 2]))
    print(are_values_equal((1, 2), (1, 2)))
    print(are_values_equal({'a': 1}, {'a': 1}))