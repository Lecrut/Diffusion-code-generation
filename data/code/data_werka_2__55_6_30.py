def validate_positive_number(value):
    if value <= 0:
        raise ValueError("All sides must be positive numbers")

def calculate_triangle_perimeter(a, b, c):
    validate_positive_number(a)
    validate_positive_number(b)
    validate_positive_number(c)
    return a + b + c

if __name__ == '__main__':
    try:
        side1 = 5
        side2 = 9
        side3 = 12
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)