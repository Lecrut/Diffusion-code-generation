from typing import Union

Number = Union[int, float]

def calculate_prism_volume(base_area: Number, height: Number) -> Number:
    return base_area * height

if __name__ == "__main__":
    hard_coded_base_area = 15.5
    hard_coded_height = 8.0
    result = calculate_prism_volume(hard_coded_base_area, hard_coded_height)
    print(result)