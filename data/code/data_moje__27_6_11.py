def check_triangle_validity(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid: sides must be positive"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid: violates triangle inequality"
    if a == b == c:
        return "Valid: equilateral"
    if a == b or b == c or a == c:
        return "Valid: isosceles"
    return "Valid: scalene"

if __name__ == '__main__':
    print(check_triangle_validity(3, 4, 5))
    print(check_triangle_validity(0, 4, 5))
    print(check_triangle_validity(1, 2, 3))
    print(check_triangle_validity(5, 5, 5))
    print(check_triangle_validity(5, 5, 8))