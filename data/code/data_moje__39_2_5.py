import math

def calculate_prism_volume(base_area, height):
    if base_area <= 0 or height <= 0:
        return 0.0
    return base_area * height

if __name__ == '__main__':
    base_area_value = 10.0
    height_value = 5.0
    volume = calculate_prism_volume(base_area_value, height_value)
    print(volume)