from typing import Tuple

def surface_area_of_rectangular_box(length: float, width: float, height: float) -> float:
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length: float = 2.5
    width: float = 3.0
    height: float = 4.0
    result: float = surface_area_of_rectangular_box(length, width, height)
    print(result)