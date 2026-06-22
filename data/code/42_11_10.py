import math
from typing import List, Tuple

def compute_ellipse_areas(axes_pairs: List[Tuple[float, float]]) -> List[float]:
    areas = []
    for major_axis, minor_axis in axes_pairs:
        if not isinstance(major_axis, (int, float)) or not isinstance(minor_axis, (int, float)):
            raise TypeError('Axis values must be numeric.')
        if major_axis <= 0 or minor_axis <= 0:
            raise ValueError('Axis values must be positive.')
        semi_major = major_axis / 2.0
        semi_minor = minor_axis / 2.0
        area = math.pi * semi_major * semi_minor
        areas.append(area)
    return areas
if __name__ == '__main__':
    sample_axes_pairs = [(10.0, 5.0), (6.0, 4.0), (8.0, 3.0)]
    computed_areas = compute_ellipse_areas(sample_axes_pairs)
    for i, area in enumerate(computed_areas):
        print(area)