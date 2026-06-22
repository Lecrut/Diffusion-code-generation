def square_scale(value: float) -> float:
    return value * value

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    squared_factor = square_scale(scale_factor)
    return base_area * squared_factor

if __name__ == '__main__':
    initial_area = 12.5
    zoom_level = 4.0
    final_area = calculate_scaled_area(initial_area, zoom_level)
    print(final_area)