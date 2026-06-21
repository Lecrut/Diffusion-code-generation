from typing import Union

def triangle_area(base: Union[int, float], height: Union[int, float]) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    base = 10
    height = 5
    area = triangle_area(base, height)
    print(area)