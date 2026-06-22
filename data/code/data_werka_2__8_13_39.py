from typing import Union

def calculate_scaled_area(base_area: Union[int, float], scale_factor: Union[int, float]) -> Union[int, float]:
    if base_area < 0 or scale_factor < 0:
        raise ValueError("Base area and scale factor must be non-negative.")
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    base_area = 10.0
    scale_factor = 2.0
    scaled_area = calculate_scaled_area(base_area, scale_factor)
    print(scaled_area)