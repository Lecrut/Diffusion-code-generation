from typing import Tuple

def surface_area(length: float, width: float, height: float) -> float:
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    result = surface_area(2.5, 3.0, 4.0)
    print(result)