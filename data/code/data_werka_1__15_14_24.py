def are_strictly_equal(value1, value2):
    return type(value1) is type(value2) and value1 == value2

if __name__ == '__main__':
    test_cases = [
        (5, 5),
        (5.0, 5),
        ('hello', 'hello'),
        ([1, 2, 3], [1, 2, 3]),
        ({'a': 1}, {'a': 1}),
        (True, False),
        (None, None),
    ]

    for value1, value2 in test_cases:
        result = are_strictly_equal(value1, value2)
        print(f"are_strictly_equal({value1!r}, {value2!r}) = {result}")