def is_larger(a, b):
    return a > b

if __name__ == '__main__':
    test_cases = [
        (10, 5),
        (3, 7),
        (-1, -2),
        (0, 0),
        (5.5, 5.4),
        (2.3, 2.3)
    ]
    
    for a, b in test_cases:
        result = is_larger(a, b)
        print(f"is_larger({a}, {b}) = {result}")