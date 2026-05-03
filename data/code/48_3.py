def is_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    return a + b > c
if __name__ == '__main__':
    test_cases = [
        ([3, 4, 5], True),
        ([1, 2, 3], False),
        ([5, 5, 5], True),
        ([1, 1, 1], True),
        ([1, 2, 4], False),
        ([6, 8, 10], True),
        ([2, 3, 5], True)
    ]
    for sides, expected in test_cases:
        result = is_triangle(sides)
        print(f"Sides: {sides}, Result: {result}, Expected: {expected}, Match: {result == expected}")