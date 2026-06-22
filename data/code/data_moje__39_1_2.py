def compute_prism_volume(base_area, height):
    if not isinstance(base_area, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base area and height must be numeric types.")
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    base_area_value = 10.5
    height_value = 5.0
    volume_result = compute_prism_volume(base_area_value, height_value)
    print(volume_result)