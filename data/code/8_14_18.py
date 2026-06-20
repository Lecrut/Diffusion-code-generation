SQUARE_POWER = 2

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    scaled_factor = scale_factor ** SQUARE_POWER
    return base_area * scaled_factor

if __name__ == '__main__':
    initial_area = 25.0
    magnification = 3.0
    final_area = calculate_scaled_area(initial_area, magnification)
    print(final_area)