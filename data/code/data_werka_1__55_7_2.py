def validate_sides(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        raise ValueError("All sides must be positive numbers")

def calculate_triangle_perimeter(a, b, c):
    validate_sides(a, b, c)
    return a + b + c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(6, 8, 10)
        print(perimeter)
    except ValueError as e:
        print(e)