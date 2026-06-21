from typing import Union

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    base_area = 10.0
    scale_factor = 2.0
    scaled_area = calculate_scaled_area(base_area, scale_factor)
    print(scaled_area)