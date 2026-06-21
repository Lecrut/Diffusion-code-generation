def is_triangle(a, b, c):
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
    print(is_triangle(3, 4, 5))
    print(is_triangle(1, 2, 3))
    print(is_triangle(10, 1, 2))
    print(is_triangle(7, 7, 7))