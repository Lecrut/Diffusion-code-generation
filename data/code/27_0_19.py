def is_valid_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

if __name__ == '__main__':
    test_cases = [
        (3, 4, 5),
        (1, 2, 3),
        (5, 5, 10),
        (6, 2, 3),
        (7, 10, 5)
    ]
    for side1, side2, side3 in test_cases:
        result = is_valid_triangle(side1, side2, side3)
        print(f"Sides ({side1}, {side2}, {side3}): {result}")