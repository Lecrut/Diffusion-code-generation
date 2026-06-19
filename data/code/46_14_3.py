def calculate_triangle_perimeter(a, b, c):
    if not all((isinstance(x, (int, float)) and x > 0 for x in [a, b, c])):
        raise ValueError('Side lengths must be positive numbers.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The given side lengths do not form a valid triangle.')
    perimeter = a + b + c
    return perimeter
if __name__ == '__main__':
    try:
        side1, side2, side3 = (6, 8, 10)
        print(calculate_triangle_perimeter(side1, side2, side3))
        side1, side2, side3 = (5, 5, 5)
        print(calculate_triangle_perimeter(side1, side2, side3))
        side1, side2, side3 = (2, 2, 4)
        print(calculate_triangle_perimeter(side1, side2, side3))
    except ValueError as e:
        print(e)