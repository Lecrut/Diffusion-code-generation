def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    test_cases = [
        (3, 4, 5, True),
        (1, 2, 3, False),
        (5, 5, 5, True),
        (10, 1, 1, False),
        (7, 7, 7, True),
        (0, 0, 0, False),
        (-1, 5, 5, False),
        (3, 4, 8, False),
        (6, 8, 10, True),
        (1, 1, 1, True)
    ]
    results = []
    for a, b, c, expected in test_cases:
        result = is_valid_triangle(a, b, c)
        results.append((a, b, c, result))
    for a, b, c, result in results:
        print(f"Sides ({a}, {b}, {c}): {result}")