def validate_sides(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        raise ValueError("All sides must be positive numbers")

def calculate_triangle_perimeter(a, b, c):
    validate_sides(a, b, c)
    perimeter = a + b + c
    return perimeter

if __name__ == '__main__':
    side1 = 5.0
    side2 = 6.0
    side3 = 7.0
    try:
        result = calculate_triangle_perimeter(side1, side2, side3)
        print(result)
    except ValueError as e:
        print(e)