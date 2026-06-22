from typing import Union

Number = Union[int, float]

def calculate_scaled_area(base_area: Number, scale_factor: Number) -> Number:
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    base = 10.0
    factor = 2.5
    result = calculate_scaled_area(base, factor)
    print(result)