def check_inequality(a, b):
    return type(a) is not type(b) or a != b

if __name__ == '__main__':
    sample_values = [
        (10, 20),
        ('hello', 'world'),
        (3.14, 3.14),
        ([], []),
        ({}, {}),
        (True, False),
        (None, None)
    ]
    
    for a, b in sample_values:
        result = check_inequality(a, b)
        print(f"check_inequality({a!r}, {b!r}) = {result}")