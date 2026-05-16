def is_valid_triangle(side_lengths):
    if len(side_lengths) != 3:
        return False
    a, b, c = side_lengths
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
if __name__ == '__main__':
    test_cases = [
        ([3, 4, 5], True),
        ([1, 2, 3], False),
        ([1, 1, 1], True),
        ([0, 4, 5], False),
        ([-1, 2, 2], False),
        ([5, 5, 10], False),
        ([2, 3, 4], True)
    ]
    for sides, expected in test_cases:
        result = is_valid_triangle(sides)
        print(f"Sides: {sides}, Result: {result}, Expected: {expected}, Match: {result == expected}")