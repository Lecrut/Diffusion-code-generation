def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid side lengths: All sides must be positive."
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle: The side lengths do not form a valid triangle."
    return a + b + c

if __name__ == '__main__':
    a = 6
    b = 8
    c = 10
    result = calculate_triangle_perimeter(a, b, c)
    print(result)