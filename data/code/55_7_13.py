def is_positive_number(x):
    return isinstance(x, (int, float)) and x > 0

def validate_triangle_sides(a, b, c):
    if not (is_positive_number(a) and is_positive_number(b) and is_positive_number(c)):
        raise ValueError("All sides must be positive numbers")

def calculate_triangle_perimeter(a, b, c):
    validate_triangle_sides(a, b, c)
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(5, 12, 13)
        print(perimeter)
    except ValueError as e:
        print(e)