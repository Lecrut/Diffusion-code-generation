def check_triangle(a, b, c):
    sides = [a, b, c]
    for s in sides:
        if s <= 0:
            return "not a triangle"
    if a + b <= c or a + c <= b or b + c <= a:
        return "not a triangle"
    if a == b == c:
        return "equilateral"
    if a == b or a == c or b == c:
        return "isosceles"
    return "scalene"

if __name__ == '__main__':
    print(check_triangle(3, 4, 5))
    print(check_triangle(5, 5, 5))
    print(check_triangle(2, 2, 3))
    print(check_triangle(1, 2, 3))
    print(check_triangle(-1, 2, 2))