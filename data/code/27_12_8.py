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
    result1 = is_valid_triangle(3, 4, 5)
    result2 = is_valid_triangle(0, 4, 5)
    result3 = is_valid_triangle(1, 2, 3)
    print(result1)
    print(result2)
    print(result3)