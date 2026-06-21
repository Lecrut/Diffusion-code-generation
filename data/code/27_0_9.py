def validate_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

if __name__ == '__main__':
    result1 = validate_triangle(3, 4, 5)
    print(result1)
    result2 = validate_triangle(1, 2, 3)
    print(result2)
    result3 = validate_triangle(-1, 5, 5)
    print(result3)