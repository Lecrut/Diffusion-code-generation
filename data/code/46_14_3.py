def calculate_triangle_perimeter(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Side lengths must be numbers.")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given side lengths do not form a valid triangle.")
    return a + b + c

if __name__ == '__main__':
    result1 = calculate_triangle_perimeter(3, 4, 5)
    result2 = calculate_triangle_perimeter(5.5, 5.5, 10)
    print(result1)
    print(result2)