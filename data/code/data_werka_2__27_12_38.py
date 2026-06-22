def is_strictly_equal(a, b):
    return type(a) == type(b) and a == b

def check_inequality(a, b):
    if not is_strictly_equal(a, b):
        return True
    return False

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
        print(result)