def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    if not isinstance(base_area, (int, float)) or not isinstance(scale_factor, (int, float)):
        raise TypeError("Inputs must be numeric")
    if base_area < 0:
        raise ValueError("Base area must be non-negative")
    scaled = scale_factor * scale_factor
    return base_area * scaled

if __name__ == '__main__':
    sample_base = 16.0
    sample_factor = 3.0
    computed_result = calculate_scaled_area(sample_base, sample_factor)
    print(computed_result)