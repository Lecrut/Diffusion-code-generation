def strict_equal(a, b):
    return type(a) == type(b) and a == b

if __name__ == '__main__':
    test_cases = [
        (1, 1),
        (1, 2),
        ('a', 'a'),
        ('a', 'b'),
        ([1, 2], [1, 2]),
        ([1, 2], [1, 3]),
        ({'key': 'value'}, {'key': 'value'}),
        ({'key': 'value'}, {'key': 'other'}),
        (1.0, 1),
        (1.0, 1.0)
    ]

    for a, b in test_cases:
        print(f"strict_equal({a}, {b}) = {strict_equal(a, b)}")