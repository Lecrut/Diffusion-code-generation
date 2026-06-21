from typing import Union

def calculate_triangle_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    area = 0.5 * base * height
    return area

if __name__ == '__main__':
    sample_base_length = 15.0
    sample_height_length = 6.0
    try:
        computed_area = calculate_triangle_area(sample_base_length, sample_height_length)
        print(computed_area)
    except ValueError as e:
        print(e)