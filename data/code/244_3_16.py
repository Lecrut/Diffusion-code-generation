def validate_dimensions(value):
    if value <= 0:
        raise ValueError("Dimensions must be positive numbers")

def trapezoid_area(base1, base2, height):
    validate_dimensions(base1)
    validate_dimensions(base2)
    validate_dimensions(height)
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    validate_dimensions(base)
    validate_dimensions(height)
    return base * height

if __name__ == '__main__':
    trapezoid = trapezoid_area(5, 7, 4)
    parallelogram = parallelogram_area(6, 3)
    print(trapezoid + parallelogram)