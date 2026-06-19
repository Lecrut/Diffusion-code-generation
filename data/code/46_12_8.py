def validate_triangle_sides(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        raise ValueError("All sides must be positive numbers.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle.")

def calculate_triangle_perimeter(a, b, c):
    validate_triangle_sides(a, b, c)
    return a + b + c

if __name__ == '__main__':
    side_a = 3.5
    side_b = 4.2
    side_c = 5.1
    perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
    print(perimeter)