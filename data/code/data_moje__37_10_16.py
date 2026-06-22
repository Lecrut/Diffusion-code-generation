from typing import Union

Number = Union[int, float]

def calculate_parallelogram_area(base: Number, height: Number) -> Number:
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return base * height

if __name__ == '__main__':
    sample_base = 10.5
    sample_height = 7.2
    area = calculate_parallelogram_area(sample_base, sample_height)
    print(area)