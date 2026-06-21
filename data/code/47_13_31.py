from typing import Dict

def triangle_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_values: Dict[str, float] = {
        'base': 15.0,
        'height': 6.0
    }
    try:
        area_result = triangle_area(sample_values['base'], sample_values['height'])
        print(area_result)
    except ValueError as e:
        print(e)