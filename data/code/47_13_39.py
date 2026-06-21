from typing import Dict

def triangle_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return 0.5 * base * height

if __name__ == '__main__':
    dimensions: Dict[str, float] = {
        'base': 15.0,
        'height': 8.0
    }
    try:
        area = triangle_area(dimensions['base'], dimensions['height'])
        print(area)
    except ValueError as e:
        print(e)