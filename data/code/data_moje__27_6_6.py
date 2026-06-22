def check_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 'Not a valid triangle: sides must be positive'
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return 'Not a valid triangle: violates triangle inequality'
    if a == b == c:
        return 'Equilateral triangle'
    if a == b or b == c or a == c:
        return 'Isosceles triangle'
    return 'Scalene triangle'
if __name__ == '__main__':
    print(check_triangle(3, 4, 5))
    print(check_triangle(3, 3, 3))
    print(check_triangle(3, 3, 4))
    print(check_triangle(1, 2, 3))
    print(check_triangle(-1, 2, 3))