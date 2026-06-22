def calculate_prism_volume(base_area, height):
    if base_area <= 0:
        raise ValueError("Base area must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")
    return base_area * height

if __name__ == '__main__':
    sample_base_area = 50.0
    sample_height = 12.5
    result = calculate_prism_volume(sample_base_area, sample_height)
    print(result)