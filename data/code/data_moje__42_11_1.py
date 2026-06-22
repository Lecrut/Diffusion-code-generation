import math
from typing import List, Tuple

def compute_ellipse_areas(axes_pairs: List[Tuple[float, float]]) -> List[float]:
    if not isinstance(axes_pairs, list):
        raise TypeError('axes_pairs must be a list of tuples')
    results = []
    for pair in axes_pairs:
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise TypeError('Each element in axes_pairs must be a tuple of two elements')
        major_axis, minor_axis = pair
        if not isinstance(major_axis, (int, float)) or not isinstance(minor_axis, (int, float)):
            raise TypeError('Axis values must be numeric (int or float)')
        if major_axis <= 0 or minor_axis <= 0:
            raise ValueError('Axis values must be positive')
        area = math.pi * major_axis * minor_axis / 4.0
        results.append(area)
    return results
if __name__ == '__main__':
    sample_axes_pairs = [(10.0, 5.0), (8.0, 3.0), (12.0, 7.0), (20.0, 20.0), (1.0, 1.0)]
    areas = compute_ellipse_areas(sample_axes_pairs)
    for major, minor, area in (zip((pair[0] for pair in sample_axes_pairs)), zip((pair[1] for pair in sample_axes_pairs)), areas):
        print(f'Ellipse with major axis {major} and minor axis {minor}: area = {area:.6f}')