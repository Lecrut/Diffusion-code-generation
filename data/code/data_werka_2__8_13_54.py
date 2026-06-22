from typing import Union

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    scale_factor_squared = scale_factor ** 2
    scaled_area_result = base_area * scale_factor_squared
    return scaled_area_result
if __name__ == '__main__':
    test_base_area = 5.0
    test_scale_factor = 3.0
    result = calculate_scaled_area(test_base_area, test_scale_factor)
    print(result)