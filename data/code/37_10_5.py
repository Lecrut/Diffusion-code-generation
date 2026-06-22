from typing import Union

Number = Union[int, float]

def calculate_parallelogram_area(base: Number, height: Number) -> Number:
    if base < 0:
        raise ValueError("Base must be non-negative")
    if height < 0:
        raise ValueError("Height must be non-negative")
    return base * height

if __name__ == '__main__':
    sample_base = 10.5
    sample_height = 4.2
    result = calculate_parallelogram_area(sample_base, sample_height)
    print(result)