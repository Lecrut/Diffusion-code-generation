def is_non_degenerate_triangle(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

if __name__ == '__main__':
    print(is_non_degenerate_triangle((3.0, 4.0, 5.0)))
    print(is_non_degenerate_triangle((1.0, 2.0, 3.0)))
    print(is_non_degenerate_triangle((1.0, 1.0, 1.0)))
    print(is_non_degenerate_triangle((-1.0, 2.0, 3.0)))
    print(is_non_degenerate_triangle((0.0, 1.0, 2.0)))