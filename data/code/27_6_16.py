def check_triangle_validity(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral triangle"
    if a == b or b == c or a == c:
        return "Isosceles triangle"
    return "Scalene triangle"

if __name__ == '__main__':
    result = check_triangle_validity(3, 3, 3)
    print(result)