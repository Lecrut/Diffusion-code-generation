def validate_triangle_sides(a, b, c):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        raise ValueError("Side lengths must be positive numbers.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given side lengths do not form a valid triangle.")

def calculate_perimeter(a, b, c):
    validate_triangle_sides(a, b, c)
    return a + b + c

if __name__ == '__main__':
    try:
        side1 = 5
        side2 = 6
        side3 = 7
        perimeter = calculate_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)