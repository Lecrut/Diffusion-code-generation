def calculate_triangle_perimeter(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle: The side lengths do not form a valid triangle."
    return a + b + c

if __name__ == '__main__':
    side1 = 7
    side2 = 10
    side3 = 5
    result = calculate_triangle_perimeter(side1, side2, side3)
    print(result)