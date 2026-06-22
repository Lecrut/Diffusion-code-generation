from typing import Tuple

def rectangular_box_surface_area(length: float, width: float, height: float) -> float:
    return 2.0 * (length * width + length * height + width * height)

if __name__ == '__main__':
    length_value: float = 2.5
    width_value: float = 3.0
    height_value: float = 4.0

    result: float = rectangular_box_surface_area(length_value, width_value, height_value)
    print(result)