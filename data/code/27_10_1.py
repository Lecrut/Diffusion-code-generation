def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    test_sides = (3.0, 4.0, 5.0)
    print(is_valid_triangle(test_sides))