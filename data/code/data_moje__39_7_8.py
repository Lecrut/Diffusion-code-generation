def calculate_prism_volume(base_area: float, height: float) -> float:
    if base_area <= 0:
        raise ValueError("Base area must be positive.")
    if height <= 0:
        raise ValueError("Height must be positive.")
    return base_area * height

if __name__ == '__main__':
    base_area_sample = 25.5
    height_sample = 10.0
    volume = calculate_prism_volume(base_area_sample, height_sample)
    print(volume)