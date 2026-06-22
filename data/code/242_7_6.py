def validate_dimensions(dimensions):
    if not all(isinstance(d, (int, float)) for d in dimensions) or len(dimensions) != 2:
        raise ValueError("Dimensions must be a list of two numbers")

def area_rhombus(d1, d2):
    validate_dimensions([d1, d2])
    return 0.5 * d1 * d2

def area_square(side):
    validate_dimensions([side])
    return side ** 2

if __name__ == '__main__':
    rhombus_area = area_rhombus(10, 8)
    square_area = area_square(6)
    print(f"Rhombus Area: {rhombus_area}")
    print(f"Square Area: {square_area}")