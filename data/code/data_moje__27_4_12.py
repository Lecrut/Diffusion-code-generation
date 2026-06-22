def is_valid_triangle(side_a: float, side_b: float, side_c: float) -> bool:
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return False
    if side_a + side_b <= side_c:
        return False
    if side_a + side_c <= side_b:
        return False
    if side_b + side_c <= side_a:
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        (3.0, 4.0, 5.0),
        (1.0, 1.0, 2.0),
        (7.0, 8.0, 9.0),
        (0.0, 1.0, 1.0),
        (2.0, 2.0, 5.0),
    ]
    for sides in test_cases:
        a, b, c = sides
        result = is_valid_triangle(a, b, c)
        print(f"{sides} -> {result}")