def check_triangle_validity(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in (a, b, c)):
        return "Invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return "Right-angled"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

if __name__ == '__main__':
    print(check_triangle_validity(3, 4, 5))
    print(check_triangle_validity(7, 7, 7))
    print(check_triangle_validity(3, 3, 4))
    print(check_triangle_validity(1, 2, 3))
    print(check_triangle_validity(10, 21, 20))
    print(check_triangle_validity(-1, 2, 2))