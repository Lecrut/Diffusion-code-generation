def check_inequality(a, b):
    if type(a) is not type(b):
        return True
    return a != b

if __name__ == '__main__':
    sample_values = [
        (5, 10),
        (5.0, 10.0),
        ('hello', 'world'),
        ([1, 2], [1, 2]),
        ({'a': 1}, {'a': 1}),
        (True, False),
        (None, None),
        (1 + 2j, 3 + 4j)
    ]
    for a, b in sample_values:
        result = check_inequality(a, b)
        print(f"check_inequality({a!r}, {b!r}) = {result}")