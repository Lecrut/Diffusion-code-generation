def calculate_triangle_perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle: Side lengths must be positive."
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle: The side lengths do not form a valid triangle."
    return a + b + c

if __name__ == '__main__':
    sides = {'side1': 6, 'side2': 8, 'side3': 10}
    result = calculate_triangle_perimeter(sides['side1'], sides['side2'], sides['side3'])
    print(result)