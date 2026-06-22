def validate_triangle(sides):
    if len(sides) != 3:
        return False
    for s in sides:
        if s <= 0:
            return False
    a, b, c = sides
    if (a + b) <= c:
        return False
    if (a + c) <= b:
        return False
    if (b + c) <= a:
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        ([3, 4, 5], True),
        ([1, 2, 3], False),
        ([0, 1, 1], False),
        ([-1, 2, 2], False),
        ([10, 1, 1], False),
        ([5, 5, 5], True)
    ]
    results = []
    for sides, expected in test_cases:
        result = validate_triangle(sides)
        results.append(result)
    print(results)