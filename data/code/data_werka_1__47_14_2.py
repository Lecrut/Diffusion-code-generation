from typing import Dict

def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    dimensions: Dict[str, float] = {
        'base': 12.0,
        'height': 8.0
    }
    area = calculate_triangle_area(dimensions['base'], dimensions['height'])
    print(area)