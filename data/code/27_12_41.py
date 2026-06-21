def check_inequality(a, b):
    if not isinstance(a, type(b)) or not isinstance(b, type(a)):
        return True
    return a != b

if __name__ == '__main__':
    test_cases = [
        (5, 10),
        (5.0, 10.0),
        ('hello', 'world'),
        ([1, 2], [3, 4]),
        ({'a': 1}, {'b': 2}),
        (True, False),
        (None, None),
        (1 + 2j, 3 + 4j)
    ]

    for a, b in test_cases:
        result = check_inequality(a, b)
        print(f"check_inequality({a!r}, {b!r}) = {result}")