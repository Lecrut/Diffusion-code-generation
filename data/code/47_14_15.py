from typing import Final
HALF: Final = 0.5

def calculate_triangle_area(base: float, height: float) -> float:
    return HALF * base * height
if __name__ == '__main__':
    base_value = 20.0
    height_value = 7.0
    area_result = calculate_triangle_area(base_value, height_value)
    print(area_result)