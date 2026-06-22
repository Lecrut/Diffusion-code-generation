def validate_dimensions(base1, base2, leg1, leg2):
    if not all(isinstance(x, (int, float)) for x in [base1, base2, leg1, leg2]):
        raise ValueError("All dimensions must be numbers.")
    if base1 <= 0 or base2 <= 0 or leg1 <= 0 or leg2 <= 0:
        raise ValueError("Dimensions must be positive.")

def calculate_perimeter(base1, base2, leg1, leg2):
    validate_dimensions(base1, base2, leg1, leg2)
    return base1 + base2 + leg1 + leg2

if __name__ == '__main__':
    try:
        perimeter = calculate_perimeter(5, 7, 3, 4)
        print(perimeter)
    except ValueError as e:
        print(e)