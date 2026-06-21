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
    result1 = is_valid_triangle(3.0, 4.0, 5.0)
    result2 = is_valid_triangle(1.0, 2.0, 10.0)
    result3 = is_valid_triangle(0.0, 5.0, 5.0)
    print(result1)
    print(result2)
    print(result3)