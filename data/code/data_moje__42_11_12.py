import math
from typing import List, Tuple, Union

AxisPair = Tuple[Union[int, float], Union[int, float]]

def calculate_ellipse_areas(pairs: List[AxisPair]) -> List[float]:
    areas = []
    for major, minor in pairs:
        if major <= 0 or minor <= 0:
            raise ValueError("Axis values must be positive")
        area = math.pi * major * minor
        areas.append(area)
    return areas

if __name__ == '__main__':
    sample_data: List[AxisPair] = [
        (10, 5),
        (3.5, 2.1),
        (100, 200),
        (7, 7)
    ]
    results = calculate_ellipse_areas(sample_data)
    for i, area in enumerate(results):
        print(f"Area {i + 1}: {area}")