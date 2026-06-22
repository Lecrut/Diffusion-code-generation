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
    val1 = 3.0
    val2 = 4.0
    val3 = 5.0
    print(is_valid_triangle(val1, val2, val3))
    print(is_valid_triangle(1.0, 2.0, 10.0))
    print(is_valid_triangle(0.0, 5.0, 5.0))
    print(is_valid_triangle(5.0, 5.0, 5.0))