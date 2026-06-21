from typing import Union

Number = Union[int, float]

def calculate_rectangle_area(width: Number, height: Number) -> Number:
    return width * height

if __name__ == '__main__':
    sample_width = 5
    sample_height = 10
    result = calculate_rectangle_area(sample_width, sample_height)
    print(result)