def are_strictly_equal(value1, value2):
    return type(value1) is type(value2) and value1 == value2
if __name__ == '__main__':
    print(are_strictly_equal(5, 5))
    print(are_strictly_equal(5, '5'))
    print(are_strictly_equal(3.0, 3))
    print(are_strictly_equal([1, 2], [1, 2]))
    print(are_strictly_equal((1, 2), (1, 2)))
    print(are_strictly_equal({1, 2}, {1, 2}))
    print(are_strictly_equal({'a': 1}, {'a': 1}))