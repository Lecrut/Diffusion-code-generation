def validate_triangle(a, b, c):
    sides = sorted((a, b, c))
    return sides[0] > 0 and sides[0] + sides[1] > sides[2]

if __name__ == '__main__':
    print(validate_triangle(3, 4, 5))
    print(validate_triangle(1, 2, 3))
    print(validate_triangle(7, 10, 5))
    print(validate_triangle(-1, 2, 3))
    print(validate_triangle(0, 0, 0))