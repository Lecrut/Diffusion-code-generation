def calculate_prism_volume(base_area: float, height: float) -> float:
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    sample_base = 25.5
    sample_height = 12.0
    result = calculate_prism_volume(sample_base, sample_height)
    print(result)