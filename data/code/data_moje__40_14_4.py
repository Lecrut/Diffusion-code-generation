from typing import Final

DIMENSIONS: Final[tuple[float, float, float]] = (2.5, 3.0, 4.0)

def calculate_rectangular_surface_area(length: float, width: float, height: float) -> float:
    if length <= 0 or width <= 0 or height <= 0:
        return 0.0
    area_top_bottom: float = length * width
    area_front_back: float = length * height
    area_left_right: float = width * height
    return 2 * (area_top_bottom + area_front_back + area_left_right)

if __name__ == '__main__':
    l, w, h = DIMENSIONS
    final_area: float = calculate_rectangular_surface_area(l, w, h)
    print(final_area)