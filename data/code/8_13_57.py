from typing import Union
SCALE_FACTOR_THRESHOLD = 1.0

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    if base_area < 0 or scale_factor < SCALE_FACTOR_THRESHOLD:
        raise ValueError('Base area must be non-negative and scale factor must be greater than or equal to 1.')
    return base_area * scale_factor ** 2
if __name__ == '__main__':
    sample_base_area = 20.0
    sample_scale_factor = 3.0
    try:
        scaled_area = calculate_scaled_area(sample_base_area, sample_scale_factor)
        print(scaled_area)
    except ValueError as e:
        print(e)