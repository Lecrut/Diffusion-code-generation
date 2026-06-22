def check_triangle_validity(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

if __name__ == '__main__':
    print(check_triangle_validity(3, 4, 5))
    print(check_triangle_validity(1, 2, 3))
    print(check_triangle_validity(-1, 2, 3))
    print(check_triangle_validity(0, 2, 3))
    print(check_triangle_validity(5, 5, 5))
    print(check_triangle_validity(1, 1, 2))
    print(check_triangle_validity(7, 10, 5))
    print(check_triangle_validity(2, 3, 4))