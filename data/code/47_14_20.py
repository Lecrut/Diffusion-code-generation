from typing import Tuple

def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    base_length = 7.0
    height_length = 3.0
    triangle_area = calculate_triangle_area(base_length, height_length)
    print(triangle_area)