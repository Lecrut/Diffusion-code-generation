is_equal_func = lambda a, b: a == b

if __name__ == '__main__':
    test_cases = [
        (5, 5),
        (3, 4),
        (7, 7),
        (8, 9),
        ('hello', 'hello'),
        ([1, 2], [1, 2])
    ]
    
    for x, y in test_cases:
        print(f"is_equal_func({x}, {y}) = {is_equal_func(x, y)}")