def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
if __name__ == '__main__':
    test_cases = [
        ([3, 4, 5], True),
        ([1, 2, 3], False),
        ([5, 5, 5], True),
        ([1, 1, 1], True),
        ([1, 2, 4], False),
        ([10, 2, 3], False)
    ]
    for sides, expected in test_cases:
        result = is_triangle(*sides)
        assert result == expected, f"Input: {sides}, Expected: {expected}, Got: {result}"
        print(f"Sides: {sides}, Is Triangle: {result}")