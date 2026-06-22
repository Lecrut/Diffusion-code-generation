from typing import Union

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    if base_area < 0 or scale_factor < 0:
        raise ValueError("Base area and scale factor must be non-negative.")
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    base_area_value = 12.5
    scale_factor_value = 3.0
    try:
        result = calculate_scaled_area(base_area_value, scale_factor_value)
        print(result)
    except ValueError as e:
        print(e)