from typing import Union

def calculate_scaled_area(base_area: Union[int, float], scale_factor: Union[int, float]) -> Union[int, float]:
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    base_area_sample = 10.0
    scale_factor_sample = 2.5
    scaled_area_result = calculate_scaled_area(base_area_sample, scale_factor_sample)
    print(scaled_area_result)