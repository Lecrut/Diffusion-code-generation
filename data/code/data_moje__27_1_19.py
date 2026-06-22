def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    print(is_valid_triangle(side1, side2, side3))
    print(is_valid_triangle(1, 2, 10))
    print(is_valid_triangle(0, 5, 5))