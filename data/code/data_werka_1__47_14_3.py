from typing import Union

def calculate_triangle_area(base: float, height: float) -> Union[float, None]:
    if base <= 0 or height <= 0:
        return None
    return 0.5 * base * height

if __name__ == '__main__':
    base = 10.0
    height = 5.0
    area = calculate_triangle_area(base, height)
    print(area)