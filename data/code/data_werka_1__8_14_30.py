from typing import Union

def calculate_scaled_area(base_area: Union[int, float], scale_factor: Union[int, float]) -> Union[int, float]:
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    sample_base_area = 10.0
    sample_scale_factor = 2.5
    result = calculate_scaled_area(sample_base_area, sample_scale_factor)
    print(result)