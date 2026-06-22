def compare_items(a, b):
    if type(a) is type(b):
        return a == b
    else:
        return False

if __name__ == '__main__':
    sample_values = [
        (10, 10),
        ('hello', 'world'),
        ([1, 2, 3], [1, 2, 3]),
        ({'key': 'value'}, {'key': 'value'}),
        (42.0, 42),
        (True, False)
    ]

    for a, b in sample_values:
        result = compare_items(a, b)
        print(f"compare_items({a}, {b}) = {result}")