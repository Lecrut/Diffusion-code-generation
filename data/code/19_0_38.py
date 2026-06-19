def is_greater(a, b):
    return a > b

if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (3, 8),
        (-1, -5),
        (0, 0),
        (7.5, 3.2),
        ('z', 'a'),
        ([1, 2], [1, 2, 3])
    ]
    
    for a, b in test_cases:
        result = is_greater(a, b)
        print(f"is_greater({a}, {b}) = {result}")