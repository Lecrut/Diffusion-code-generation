def strict_equal(a, b):
    return type(a) == type(b) and a == b

if __name__ == '__main__':
    test_cases = [
        (1, 1),
        (1, '1'),
        ('hello', 'hello'),
        ('hello', 'world'),
        (3.14, 3.14),
        (3.14, 3),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 4]),
        ({'a': 1}, {'a': 1}),
        ({'a': 1}, {'b': 1})
    ]

    for a, b in test_cases:
        print(f"strict_equal({a}, {b}) = {strict_equal(a, b)}")