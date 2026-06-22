import math
from typing import List, Tuple

def compute_ellipse_areas(axes: List[Tuple[float, float]]) -> List[float]:
    if not isinstance(axes, list):
        raise TypeError('Input must be a list of tuples.')
    areas: List[float] = []
    for pair in axes:
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise ValueError('Each axis pair must be a tuple of two floats.')
        a, b = pair
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('Axis values must be numeric.')
        if a < 0 or b < 0:
            raise ValueError('Axis lengths must be non-negative.')
        area = math.pi * a * b
        areas.append(area)
    return areas
if __name__ == '__main__':
    sample_axes: List[Tuple[float, float]] = [(5.0, 3.0), (10.0, 7.0), (1.0, 1.0)]
    results = compute_ellipse_areas(sample_axes)
    for axis, area in zip(sample_axes, results):
        print(f'Ellipse with axes {axis}: Area = {area}')