def check_triangle_validity(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalid"
    if a == b and b == c:
        return "equilateral"
    if a == b or a == c or b == c:
        return "isosceles"
    return "scalene"

if __name__ == '__main__':
    print(check_triangle_validity(3, 4, 5))
    print(check_triangle_validity(3, 3, 3))
    print(check_triangle_validity(3, 3, 4))
    print(check_triangle_validity(1, 2, 3))