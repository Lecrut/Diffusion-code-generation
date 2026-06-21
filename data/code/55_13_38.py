def validate_side_length(side):
    if not isinstance(side, (int, float)):
        raise ValueError("All sides must be numeric types.")
    if side <= 0:
        raise ValueError("Side lengths must be positive numbers.")

def calculate_triangle_perimeter(a, b, c):
    validate_side_length(a)
    validate_side_length(b)
    validate_side_length(c)
    return a + b + c

if __name__ == '__main__':
    try:
        side1 = 5.0
        side2 = 6.0
        side3 = 7.0
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)