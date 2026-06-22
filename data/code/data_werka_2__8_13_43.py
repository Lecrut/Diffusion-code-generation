from typing import Union

def validate_input(base_area: float, scale_factor: float) -> None:
    if base_area < 0:
        raise ValueError("Base area must be non-negative.")
    if scale_factor < 0:
        raise ValueError("Scale factor must be non-negative.")

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    validate_input(base_area, scale_factor)
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    sample_base_area = 12.5
    sample_scale_factor = 3.0
    try:
        scaled_area = calculate_scaled_area(sample_base_area, sample_scale_factor)
        print(scaled_area)
    except ValueError as e:
        print(e)