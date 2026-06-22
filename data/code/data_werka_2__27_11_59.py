def values_differ(a, b):
    return a != b

if __name__ == '__main__':
    sample_values = [
        (10, 20),
        ('hello', 'world'),
        ([1, 2], [1, 3]),
        ({'a': 1}, {'b': 1}),
        (3.14, 3.15)
    ]
    
    for a, b in sample_values:
        print(values_differ(a, b))