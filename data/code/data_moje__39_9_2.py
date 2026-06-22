from typing import Union

Number = Union[int, float]

def calculate_prism_volume(base_area: Number, height: Number) -> Number:
    return base_area * height

if __name__ == '__main__':
    sample_base_area = 25
    sample_height = 10
    result = calculate_prism_volume(sample_base_area, sample_height)
    print(result)