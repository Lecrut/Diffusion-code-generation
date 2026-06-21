def values_differ(a, b):
    return a != b

if __name__ == '__main__':
    sample_values = [
        (10, 20),
        ('hello', 'world'),
        ([1, 2], [3, 4]),
        ({'a': 1}, {'b': 1}),
        (3.14, 2.71)
    ]

    for a, b in sample_values:
        print(values_differ(a, b))