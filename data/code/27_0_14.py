def validate_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    print(validate_triangle(3, 4, 5))
    print(validate_triangle(1, 2, 3))
    print(validate_triangle(7, 10, 5))
    print(validate_triangle(0, 1, 1))
    print(validate_triangle(-1, 2, 3))