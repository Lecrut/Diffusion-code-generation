def validate_positive(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def calculate_surface_area(base_side, slant_height):
    validate_positive(base_side, "base_side")
    validate_positive(slant_height, "slant_height")
    base_area = base_side ** 2
    slant_area = 2 * base_side * slant_height
    return base_area + slant_area

if __name__ == '__main__':
    result = calculate_surface_area(5, 7)
    print(result)