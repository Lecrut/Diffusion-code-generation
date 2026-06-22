from typing import Union

def calculate_area(length: float, width: float) -> float:
    if length <= 0 or width <= 0:
        return 0.0
    return length * width

if __name__ == '__main__':
    length_rect = 12.5
    width_rect = 4.0
    area_rect = calculate_area(length_rect, width_rect)
    print(area_rect)