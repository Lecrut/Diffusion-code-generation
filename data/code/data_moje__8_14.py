def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    base_area_value = 10.0
    scale_factor_value = 2.5
    result = calculate_scaled_area(base_area_value, scale_factor_value)
    print(result)