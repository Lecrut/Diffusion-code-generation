import math

UNIT_SCALE = {"cm": 1, "mm": 10, "m": 0.01}

def get_scaled_radius(value, unit_key):
    scale_factor = UNIT_SCALE.get(unit_key, 1)
    return value * scale_factor

def compute_area(radius):
    return math.pi * radius ** 2

def circle_area_from_radius_and_unit(value, unit_key):
    scaled = get_scaled_radius(value, unit_key)
    return compute_area(scaled)

if __name__ == '__main__':
    input_value = 7
    input_unit = "cm"
    result = circle_area_from_radius_and_unit(input_value, input_unit)
    print(result)