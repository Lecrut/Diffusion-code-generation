def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    squared_factor = scale_factor * scale_factor
    final_area = base_area * squared_factor
    return final_area

if __name__ == '__main__':
    initial_area = 50.0
    expansion_ratio = 1.5
    output_value = calculate_scaled_area(initial_area, expansion_ratio)
    print(output_value)