def are_strictly_equal(value1, value2):
    return type(value1) is type(value2) and value1 == value2

if __name__ == '__main__':
    test_cases = [
        (42, 42),
        (42, '42'),
        ('hello', 'hello'),
        ('hello', "hello"),
        ([1, 2, 3], [1, 2, 3]),
        ({'a': 1}, {'a': 1}),
        (1.0, 1),
        (True, 1),
    ]

    for value1, value2 in test_cases:
        result = are_strictly_equal(value1, value2)
        print(f"are_strictly_equal({value1}, {value2}) = {result}")