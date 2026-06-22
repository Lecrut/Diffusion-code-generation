def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    squared_scale = scale_factor * scale_factor
    final_area = base_area * squared_scale
    return final_area

if __name__ == '__main__':
    initial_area = 125.5
    multiplier = 4.0
    output = calculate_scaled_area(initial_area, multiplier)
    print(output)