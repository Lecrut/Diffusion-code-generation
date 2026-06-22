import math
from typing import List, Tuple

def compute_ellipse_areas(major_axes: List[float], minor_axes: List[float]) -> List[float]:
    if len(major_axes) != len(minor_axes):
        raise ValueError("Major and minor axes lists must have the same length")

    areas = []
    for major, minor in zip(major_axes, minor_axes):
        if not isinstance(major, (int, float)) or not isinstance(minor, (int, float)):
            raise TypeError("Axis values must be numeric")
        if major < 0 or minor < 0:
            raise ValueError("Axis values must be non-negative")
        area = math.pi * major * minor
        areas.append(area)
    return areas

def process_single_ellipse(major_axis: float, minor_axis: float) -> float:
    if not isinstance(major_axis, (int, float)) or not isinstance(minor_axis, (int, float)):
        raise TypeError("Axis values must be numeric")
    if major_axis < 0 or minor_axis < 0:
        raise ValueError("Axis values must be non-negative")
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    sample_major_axes = [5.0, 10.0, 3.5, 7.2]
    sample_minor_axes = [3.0, 4.0, 2.1, 5.5]

    areas = compute_ellipse_areas(sample_major_axes, sample_minor_axes)
    print(areas)

    single_area = process_single_ellipse(8.0, 6.0)
    print(single_area)