def validate_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    print(validate_triangle(3, 4, 5))
    print(validate_triangle(1, 2, 3))
    print(validate_triangle(10, 10, 10))
    print(validate_triangle(1, 1, 3))
    print(validate_triangle(0, 4, 5))