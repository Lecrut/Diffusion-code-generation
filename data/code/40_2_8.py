from typing import Union

Number = Union[int, float]

def calculate_surface_area(length: Number, width: Number, height: Number) -> float:
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers")
    return float(2 * (length * width + length * height + width * height))

if __name__ == '__main__':
    l = 10
    w = 5
    h = 3
    result = calculate_surface_area(l, w, h)
    print(result)