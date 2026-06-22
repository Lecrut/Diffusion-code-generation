def is_valid_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and all(side > 0 for side in sides)

if __name__ == '__main__':
    print(is_valid_triangle((3.0, 4.0, 5.0)))
    print(is_valid_triangle((1.0, 2.0, 3.0)))
    print(is_valid_triangle((0.0, 4.0, 5.0)))