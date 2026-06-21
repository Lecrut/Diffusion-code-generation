def check_triangle_validity(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    if a == b and b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    print(check_triangle_validity(side1, side2, side3))