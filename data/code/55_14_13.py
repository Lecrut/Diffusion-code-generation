def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All sides must be numeric types.")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers.")
    perimeter = a + b + c
    return perimeter

if __name__ == '__main__':
    try:
        side1, side2, side3 = 5.0, 6.0, 7.0
        result = calculate_triangle_perimeter(side1, side2, side3)
        print(result)
    except ValueError as e:
        print(e)