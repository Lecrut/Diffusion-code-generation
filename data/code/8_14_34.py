def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    sample_base_area = 10.0
    sample_scale_factor = 2.0
    scaled_area = calculate_scaled_area(sample_base_area, sample_scale_factor)
    print(scaled_area)