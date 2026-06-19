def validate_numbers(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise ValueError("All inputs must be numbers.")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides of a triangle must be positive.")

def calculate_triangle_perimeter(a, b, c):
    validate_numbers(a, b, c)
    return a + b + c

if __name__ == '__main__':
    side1 = 7.5
    side2 = 9.3
    side3 = 5.8
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)