def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    return False

if __name__ == '__main__':
    result = is_valid_triangle(3, 4, 5)
    print(result)
    result2 = is_valid_triangle(0, 0, 0)
    print(result2)
    result3 = is_valid_triangle(1, 2, 3)
    print(result3)