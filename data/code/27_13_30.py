def check_inequality(a, b):
    return type(a) is not type(b) or a != b

if __name__ == '__main__':
    sample_values = [
        (5, 10),
        (3.14, 3.14),
        ('hello', 'world'),
        ([1, 2], [1, 2]),
        ({'a': 1}, {'a': 1}),
        (True, False),
        (None, None)
    ]
    
    for a, b in sample_values:
        print(f"check_inequality({a}, {b}) = {check_inequality(a, b)}")