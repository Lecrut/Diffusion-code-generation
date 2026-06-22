import math

def total_surface_area_cone(base_side, slant_height):
    radius = base_side / 2.0
    base_area = math.pi * (radius ** 2)
    lateral_area = math.pi * radius * slant_height
    return base_area + lateral_area

if __name__ == '__main__':
    base_side_value = 10.0
    slant_height_value = 13.0
    result = total_surface_area_cone(base_side_value, slant_height_value)
    print(result)