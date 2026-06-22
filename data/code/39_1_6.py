def calculate_prism_volume(base_area: float, height: float) -> float:
    if base_area < 0:
        raise ValueError("Base area must be non-negative")
    if height < 0:
        raise ValueError("Height must be non-negative")
    return base_area * height

if __name__ == '__main__':
    sample_base_area = 25.5
    sample_height = 10.0
    result = calculate_prism_volume(sample_base_area, sample_height)
    print(result)