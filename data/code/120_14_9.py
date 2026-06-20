def fast_compare(a, b):
    return a == b

if __name__ == '__main__':
    test_cases = [
        (5, 5),
        (10, 20),
        ('hello', 'hello'),
        ('hello', 'world'),
        (1, 2),
        ([1, 2], [1, 2]),
        ({'a': 1}, {'a': 1}),
        (None, None),
        (10, '10')
    ]

    for x, y in test_cases:
        print(fast_compare(x, y))