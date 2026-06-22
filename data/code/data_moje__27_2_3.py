def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

if __name__ == '__main__':
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 2, 3))
    print(is_valid_triangle(-1, 2, 3))
    print(is_valid_triangle(0, 5, 5))
    print(is_valid_triangle(7, 10, 5))
    print(is_valid_triangle(1, 1, 1))
    print(is_valid_triangle(10, 2, 2))
    print(is_valid_triangle(2, 2, 10))
    print(is_valid_triangle(5, 5, 0))
    print(is_valid_triangle(100, 100, 100))