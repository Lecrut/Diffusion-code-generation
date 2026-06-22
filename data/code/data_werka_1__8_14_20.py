from typing import Union

def calculate_scaled_area(base_area: Union[int, float], scale_factor: Union[int, float]) -> Union[int, float]:
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    base_area = 100.0
    scale_factor = 2.5
    scaled_area = calculate_scaled_area(base_area, scale_factor)
    print(scaled_area)