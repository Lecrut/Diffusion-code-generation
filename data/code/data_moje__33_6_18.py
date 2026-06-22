from typing import Union

Number = Union[int, float]

def calculate_triangle_area(base: Number, height: Number) -> Number:
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base: Number = 10
    sample_height: Number = 5
    area_result = calculate_triangle_area(sample_base, sample_height)
    print(area_result)