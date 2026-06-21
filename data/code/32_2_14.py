from typing import Union

Dimensions = Union[int, float]

DEFAULT_WIDTH: Dimensions = 4
DEFAULT_HEIGHT: Dimensions = 6
SCALE_FACTOR: float = 1.0

def compute_rect_area(width: Dimensions, height: Dimensions) -> float:
    return float(width * height) * SCALE_FACTOR

if __name__ == '__main__':
    w: Dimensions = DEFAULT_WIDTH
    h: Dimensions = DEFAULT_HEIGHT
    calculated_area: float = compute_rect_area(w, h)
    print(calculated_area)