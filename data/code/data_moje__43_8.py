def validate_parameters(base_side, slant_height):
    if not isinstance(base_side, (int, float)):
        raise TypeError("base_side must be a number")
    if not isinstance(slant_height, (int, float)):
        raise TypeError("slant_height must be a number")
    if base_side <= 0:
        raise ValueError("base_side must be positive")
    if slant_height <= 0:
        raise ValueError("slant_height must be positive")

def calculate_surface_area(base_side, slant_height):
    validate_parameters(base_side, slant_height)
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    side = 5
    height = 8
    result = calculate_surface_area(side, height)
    print(result)
    side = 10
    height = 6
    result = calculate_surface_area(side, height)
    print(result)