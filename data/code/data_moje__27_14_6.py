def validate_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

if __name__ == '__main__':
    print(validate_triangle(3, 4, 5))
    print(validate_triangle(1, 2, 3))
    print(validate_triangle(7, 10, 5))
    print(validate_triangle(0, 4, 5))
    print(validate_triangle(-1, 2, 3))