def strict_equal(value1, value2):
    return type(value1) is type(value2) and value1 == value2

if __name__ == '__main__':
    test_cases = [
        (42, 42),
        (3.14, 3.14),
        ("hello", "hello"),
        ([1, 2, 3], [1, 2, 3]),
        ((1, 2), (1, 2)),
        ({'a': 1}, {'a': 1}),
        (True, True),
        (None, None),
        (42, "42"),
        (3.14, 3),
    ]

    results = [strict_equal(value1, value2) for value1, value2 in test_cases]
    print(results)