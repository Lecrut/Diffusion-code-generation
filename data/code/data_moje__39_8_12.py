def calculate_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return base_area * height

if __name__ == '__main__':
    base_area_value = 25.0
    height_value = 10.0
    result = calculate_prism_volume(base_area_value, height_value)
    print(result)