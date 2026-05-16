def is_triangle(sidea, sideb, sidec):
    if sidea + sideb > sidec and sidea + sidec > sideb and sideb + sidec > sidea:
        return True
    else:
        return False
if __name__ == '__main__':
    test_cases = [
        ([3, 4, 5], True),
        ([1, 2, 3], False),
        ([5, 5, 5], True),
        ([1, 1, 1], True),
        ([1, 2, 4], False),
        ([0, 1, 1], False)
    ]
    for sides, expected in test_cases:
        result = is_triangle(*sides)
        assert result == expected, f"Input: {sides}, Expected: {expected}, Got: {result}"
        print(f"Sides: {sides}, Result: {result}")