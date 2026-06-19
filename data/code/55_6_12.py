def calculate_triangle_perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in (a, b, c)):
        raise ValueError("All sides must be positive numbers")
    return a + b + c

if __name__ == '__main__':
    try:
        side1 = 7
        side2 = 9
        side3 = 5
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)