def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
if __name__ == '__main__':
    test_cases = [
        ([3, 4, 5], True),
        ([1, 2, 3], False),
        ([5, 5, 5], True),
        ([1, 1, 10], False),
        ([6, 8, 10], True),
        ([2, 3, 4], True),
        ([0, 5, 5], False)
    ]
    for sides, expected in test_cases:
        result = is_triangle(*sides)
        assert result == expected, f"Sides: {sides}, Expected: {expected}, Got: {result}"
        print(f"Sides: {sides}, Result: {result}")