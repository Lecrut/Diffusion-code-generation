def is_valid_triangle(side_a, side_b, side_c):
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return False
    return (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a)

if __name__ == '__main__':
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 2, 3))
    print(is_valid_triangle(-1, 2, 2))
    print(is_valid_triangle(0, 0, 0))
    print(is_valid_triangle(5, 5, 5))