import math

def calculate_square_pyramid_surface_area(base_length, lateral_edge):
    if base_length <= 0 or lateral_edge <= 0:
        raise ValueError("Dimensions must be positive")

    base_area = base_length ** 2

    half_base = base_length / 2
    slant_height = math.sqrt(lateral_edge ** 2 - half_base ** 2)

    if slant_height <= 0:
        raise ValueError("Invalid dimensions: lateral edge too short for given base")

    lateral_area = 4 * (0.5 * base_length * slant_height)

    return base_area + lateral_area

if __name__ == '__main__':
    base = 4
    lateral = 5
    area = calculate_square_pyramid_surface_area(base, lateral)
    print(area)