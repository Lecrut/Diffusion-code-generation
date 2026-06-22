def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    test_cases = [
        (3, 4, 5),
        (1, 2, 3),
        (10, 5, 2),
        (7, 7, 7),
        (0, 4, 5),
        (-1, 2, 3)
    ]
    for side1, side2, side3 in test_cases:
        result = is_valid_triangle(side1, side2, side3)
        print(f"Sides: {side1}, {side2}, {side3} -> Valid: {result}")