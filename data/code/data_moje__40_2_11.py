from typing import Tuple

def calculate_surface_area(length: float, width: float, height: float) -> float:
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    length = 10.0
    width = 5.0
    height = 3.0
    result = calculate_surface_area(length, width, height)
    print(result)