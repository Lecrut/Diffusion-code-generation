def calculate_slant_height(base_side, height):
    if base_side <= 0 or height <= 0:
        raise ValueError("Base side and height must be positive values")
    half_base = base_side / 2
    return (half_base ** 2 + height ** 2) ** 0.5

def calculate_surface_area(base_side, height):
    slant_height = calculate_slant_height(base_side, height)
    base_area = base_side ** 2
    lateral_area = 2 * base_side * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base = 6.0
    perp_height = 4.0
    result = calculate_surface_area(base, perp_height)
    print(result)