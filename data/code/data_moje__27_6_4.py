def check_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a valid triangle"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

if __name__ == '__main__':
    print(check_triangle(3, 3, 3))
    print(check_triangle(3, 4, 4))
    print(check_triangle(3, 4, 5))
    print(check_triangle(1, 2, 3))
    print(check_triangle(-1, 2, 2))