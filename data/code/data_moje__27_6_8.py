def triangle_status(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return "invalid"
    if sides[0] + sides[1] <= sides[2]:
        return "not_a_triangle"
    if sides[0] == sides[1] == sides[2]:
        return "equilateral"
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return "isosceles"
    return "scalene"

if __name__ == '__main__':
    print(triangle_status(3, 4, 5))
    print(triangle_status(2, 2, 2))
    print(triangle_status(1, 1, 2))
    print(triangle_status(10, 2, 10))
    print(triangle_status(-1, 2, 3))