def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    squared_scale = scale_factor * scale_factor
    scaled_result = base_area * squared_scale
    return scaled_result

if __name__ == '__main__':
    area_base = 15.0
    factor_val = 3.0
    output_value = calculate_scaled_area(area_base, factor_val)
    print(output_value)