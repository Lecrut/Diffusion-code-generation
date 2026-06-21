def validate_triangle(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] <= 0:
        return False
    return sides[0] + sides[1] > sides[2]

if __name__ == '__main__':
    a1, b1, c1 = 3, 4, 5
    a2, b2, c2 = 1, 2, 3
    a3, b3, c3 = 0.5, 0.6, 0.7
    print(validate_triangle(a1, b1, c1))
    print(validate_triangle(a2, b2, c2))
    print(validate_triangle(a3, b3, c3))
    print(validate_triangle(1, -2, 3))
    print(validate_triangle(10, 10, 10))
    print(validate_triangle(7, 2, 8))