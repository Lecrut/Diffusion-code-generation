def is_valid_triangle(side_a, side_b, side_c):
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
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 2, 3))
    print(is_valid_triangle(10, 1, 2))
    print(is_valid_triangle(7, 10, 5))