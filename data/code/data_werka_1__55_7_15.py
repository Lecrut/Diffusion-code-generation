def validate_side_length(side):
    if not isinstance(side, (int, float)) or side <= 0:
        raise ValueError("All sides must be positive numbers")

def calculate_triangle_perimeter(a, b, c):
    validate_side_length(a)
    validate_side_length(b)
    validate_side_length(c)
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(5, 12, 13)
        print(perimeter)
    except ValueError as e:
        print(e)