from typing import Union
THRESHOLD = 0.0

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    if base_area < THRESHOLD or scale_factor < THRESHOLD:
        raise ValueError('Base area and scale factor must be non-negative.')
    return base_area * scale_factor ** 2
if __name__ == '__main__':
    sample_base_area = 12.5
    sample_scale_factor = 3.0
    try:
        scaled_area = calculate_scaled_area(sample_base_area, sample_scale_factor)
        print(scaled_area)
    except ValueError as e:
        print(e)