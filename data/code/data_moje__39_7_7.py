def calculate_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    sample_base_area = 15.5
    sample_height = 10.0
    result = calculate_prism_volume(sample_base_area, sample_height)
    print(result)