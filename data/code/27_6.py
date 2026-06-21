def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "not a triangle"
    if a == b and b == c:
        return "equilateral"
    if a == b or a == c or b == c:
        return "isosceles"
    return "scalene"

if __name__ == '__main__':
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(0, 0, 0))
    print(classify_triangle(5, 5, 5))