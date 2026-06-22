import math

DIMENSION_LABELS = {"length": 0, "width": 1, "height": 2}

def calculate_rectangular_box_surface_area(length, width, height):
    dimensions = [length, width, height]
    area_pair_1 = dimensions[DIMENSION_LABELS["length"]] * dimensions[DIMENSION_LABELS["width"]]
    area_pair_2 = dimensions[DIMENSION_LABELS["width"]] * dimensions[DIMENSION_LABELS["height"]]
    area_pair_3 = dimensions[DIMENSION_LABELS["height"]] * dimensions[DIMENSION_LABELS["length"]]
    return 2 * (area_pair_1 + area_pair_2 + area_pair_3)

if __name__ == '__main__':
    l_val = 12.5
    w_val = 7.0
    h_val = 3.5
    surface_area_value = calculate_rectangular_box_surface_area(l_val, w_val, h_val)
    print(surface_area_value)