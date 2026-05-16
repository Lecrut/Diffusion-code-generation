def is_valid_triangle(side_lengths):
    if len(side_lengths) != 3:
        return False
    a = side_lengths[0]
    b = side_lengths[1]
    c = side_lengths[2]
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
        ([1, 2, 4], False),
        ([0, 4, 5], False),
        ([-1, 2, 3], False),
        ([5, 5, 0], False),
        ([2, 3, 4], True)
    ]
    for sides, expected in test_cases:
        result = is_valid_triangle(sides)
        print(f"Sides: {sides}, Expected: {expected}, Got: {result}, Match: {result == expected}")