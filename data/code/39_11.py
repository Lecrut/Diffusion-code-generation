def calculate_prism_volume(base_area, height):
    if base_area <= 0 or height <= 0:
        return 0
    return base_area * height

if __name__ == '__main__':
    base_area_val = 10
    height_val = 5
    volume = calculate_prism_volume(base_area_val, height_val)
    print(volume)