def check_triangle_validity(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return "invalid"
    if sides[0] == sides[1] == sides[2]:
        return "equilateral"
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return "isosceles"
    return "scalene"

if __name__ == '__main__':
    print(check_triangle_validity(3, 4, 5))
    print(check_triangle_validity(2, 2, 2))
    print(check_triangle_validity(1, 2, 10))