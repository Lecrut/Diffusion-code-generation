from typing import Tuple

def surface_area_of_box(width: float, height: float, depth: float) -> float:
    return 2.0 * (width * height + width * depth + height * depth)

if __name__ == '__main__':
    w: float = 2.5
    h: float = 3.0
    d: float = 4.0
    result: float = surface_area_of_box(w, h, d)
    print(result)