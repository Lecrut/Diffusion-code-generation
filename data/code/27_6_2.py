def triangle_status(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid: sides must be positive"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid: violates triangle inequality"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

if __name__ == '__main__':
    print(triangle_status(3, 4, 5))
    print(triangle_status(5, 5, 5))
    print(triangle_status(5, 5, 8))
    print(triangle_status(1, 2, 3))
    print(triangle_status(-1, 2, 3))