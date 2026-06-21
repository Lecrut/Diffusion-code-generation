MIN_SIDE_THRESHOLD = 0
STRICT_DEGENERACY_LIMIT = 0

def is_valid_triangle(side_a: float, side_b: float, side_c: float) -> bool:
    if side_a <= MIN_SIDE_THRESHOLD or side_b <= MIN_SIDE_THRESHOLD or side_c <= MIN_SIDE_THRESHOLD:
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
        (5, 12, 13),
        (1, 1, 2),
        (0, 5, 5),
        (-3, 4, 5),
        (7, 8, 9),
        (2.5, 2.5, 5.0)
    ]
    for x, y, z in test_cases:
        print(is_valid_triangle(x, y, z))