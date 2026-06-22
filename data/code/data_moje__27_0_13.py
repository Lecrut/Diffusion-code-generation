def is_valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    test_cases = [
        (3, 4, 5, True),
        (1, 2, 3, False),
        (7, 10, 5, True),
        (0, 0, 0, False),
        (10, 1, 1, False),
        (5, 5, 5, True),
        (1, 1, 100, False)
    ]

    results = []
    for a, b, c, expected in test_cases:
        result = is_valid_triangle(a, b, c)
        results.append((a, b, c, result))

    for a, b, c, result in results:
        print(f"is_valid_triangle({a}, {b}, {c}) -> {result}")