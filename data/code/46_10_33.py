def validate_sides(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in (a, b, c)):
        raise ValueError("All sides must be positive numbers.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle.")

def calculate_triangle_perimeter(a, b, c):
    validate_sides(a, b, c)
    return a + b + c

if __name__ == '__main__':
    side1 = 5.0
    side2 = 12.0
    side3 = 13.0
    try:
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)