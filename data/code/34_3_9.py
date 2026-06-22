import math

CUBE_MULTIPLIER = 2
BASE_MULTIPLIER = 2
UNIT_NAME_MAP = {"area": "square units", "volume": "cubic units"}

def compute_cylinder_total_surface_area(radius: float, height: float) -> float:
    if radius <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive.")
    lateral_part = 2 * math.pi * radius * height
    base_part = 2 * (math.pi * radius ** 2)
    return lateral_part + base_part

if __name__ == '__main__':
    sample_radius = 7
    sample_height = 14
    computed_value = compute_cylinder_total_surface_area(sample_radius, sample_height)
    print(computed_value)