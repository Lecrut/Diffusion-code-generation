def validate_dimensions(base1, base2, height):
    if not all(isinstance(x, (int, float)) for x in [base1, base2, height]):
        raise ValueError("All dimensions must be numbers")
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")

def trapezoid_area(base1, base2, height):
    validate_dimensions(base1, base2, height)
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    validate_dimensions(base, height, 1)
    return base * height

if __name__ == '__main__':
    trapezoid = trapezoid_area(5, 7, 4)
    parallelogram = parallelogram_area(6, 3)
    print(trapezoid + parallelogram)