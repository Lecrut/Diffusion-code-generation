def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c and a > 0 and b > 0 and c > 0

if __name__ == '__main__':
    test_cases = [(3, 4, 5), (1, 2, 3), (7, 10, 5), (-1, 2, 3), (0, 0, 0)]
    results = [is_valid_triangle(case) for case in test_cases]
    for case, result in zip(test_cases, results):
        print(f"{case}: {result}")