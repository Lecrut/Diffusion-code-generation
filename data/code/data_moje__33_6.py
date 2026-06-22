from typing import Union

Number = Union[int, float]

def calculate_triangle_area(base: Number, height: Number) -> Number:
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    area = calculate_triangle_area(sample_base, sample_height)
    print(area)