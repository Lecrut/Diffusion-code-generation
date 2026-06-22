def _compute_scale_factor_squared(scale_factor: float) -> float:
    squared_value = scale_factor * scale_factor
    return squared_value

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    if base_area < 0:
        raise ValueError("Base area cannot be negative")
    squared_factor = _compute_scale_factor_squared(scale_factor)
    return base_area * squared_factor

if __name__ == '__main__':
    INITIAL_AREA = 25.0
    EXPANSION_FACTOR = 1.5
    final_value = calculate_scaled_area(INITIAL_AREA, EXPANSION_FACTOR)
    print(final_value)