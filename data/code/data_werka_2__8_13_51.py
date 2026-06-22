from typing import Union

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    if base_area < 0 or scale_factor < 0:
        raise ValueError("Base area and scale factor must be non-negative.")
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    BASE_AREA = 15.0
    SCALE_FACTOR = 2.0
    try:
        scaled_area = calculate_scaled_area(BASE_AREA, SCALE_FACTOR)
        print(scaled_area)
    except ValueError as e:
        print(e)