from typing import Union

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    if base_area < 0 or scale_factor < 0:
        raise ValueError("Base area and scale factor must be non-negative.")
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    base_area_sample = 10.0
    scale_factor_sample = 2.0
    scaled_area_result = calculate_scaled_area(base_area_sample, scale_factor_sample)
    print(scaled_area_result)