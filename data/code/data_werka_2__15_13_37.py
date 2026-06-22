def are_strictly_equal(value1, value2):
    return type(value1) == type(value2) and value1 == value2
if __name__ == '__main__':
    print(are_strictly_equal(42, 42))
    print(are_strictly_equal(42, '42'))
    print(are_strictly_equal(3.14, 3.14))
    print(are_strictly_equal(3.14, '3.14'))
    print(are_strictly_equal([1, 2, 3], [1, 2, 3]))
    print(are_strictly_equal((1, 2, 3), (1, 2, 3)))
    print(are_strictly_equal({1, 2, 3}, {1, 2, 3}))
    print(are_strictly_equal({'a': 1}, {'a': 1}))