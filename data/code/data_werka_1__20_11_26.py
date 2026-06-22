def compare_items(a, b):
    if type(a) is type(b):
        return a == b
    return False

if __name__ == '__main__':
    sample_values = [
        (10, 20),
        (3.14, 3.14),
        ('hello', 'world'),
        ([1, 2, 3], [1, 2, 3]),
        ({'key': 'value'}, {'key': 'value'}),
        (True, False),
        (None, None)
    ]

    for a, b in sample_values:
        print(f"compare_items({a}, {b}) = {compare_items(a, b)}")