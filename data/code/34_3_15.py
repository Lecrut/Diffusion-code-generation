import math

TWO = 2
MINIMUM_DIMENSION = 0.0

def calculate_cylinder_surface_area(radius, height):
    if radius < MINIMUM_DIMENSION or height < MINIMUM_DIMENSION:
        raise ValueError("Dimensions must be non-negative")
    base_area = math.pi * radius ** TWO
    lateral_area = TWO * math.pi * radius * height
    return TWO * base_area + lateral_area

if __name__ == '__main__':
    sample_radius = 7.5
    sample_height = 12.0
    computed_area = calculate_cylinder_surface_area(sample_radius, sample_height)
    print(computed_area)