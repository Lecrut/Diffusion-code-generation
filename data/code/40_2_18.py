from typing import Tuple

def calculate_surface_area(length: float, width: float, height: float) -> float:
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    l: float = 5.0
    w: float = 3.0
    h: float = 4.0
    area: float = calculate_surface_area(l, w, h)
    print(area)