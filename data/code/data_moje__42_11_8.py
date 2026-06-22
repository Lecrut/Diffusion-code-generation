import math
from typing import List, Tuple

def compute_ellipse_areas(major_axes: List[float], minor_axes: List[float]) -> List[float]:
    if len(major_axes) != len(minor_axes):
        raise ValueError("Major and minor axis lists must have the same length.")
    if any(not isinstance(a, (int, float)) for a in major_axes):
        raise TypeError("Major axis values must be numeric.")
    if any(not isinstance(b, (int, float)) for b in minor_axes):
        raise TypeError("Minor axis values must be numeric.")
    if any(a <= 0 for a in major_axes):
        raise ValueError("Major axis values must be positive.")
    if any(b <= 0 for b in minor_axes):
        raise ValueError("Minor axis values must be positive.")
    return [math.pi * a * b for a, b in zip(major_axes, minor_axes)]

def compute_ellipse_area_single(major_axis: float, minor_axis: float) -> float:
    if not isinstance(major_axis, (int, float)):
        raise TypeError("Major axis must be numeric.")
    if not isinstance(minor_axis, (int, float)):
        raise TypeError("Minor axis must be numeric.")
    if major_axis <= 0:
        raise ValueError("Major axis must be positive.")
    if minor_axis <= 0:
        raise ValueError("Minor axis must be positive.")
    return math.pi * major_axis * minor_axis

if __name__ == '__main__':
    major_values = [5.0, 3.0, 10.0, 7.5]
    minor_values = [3.0, 2.0, 5.0, 4.0]
    areas = compute_ellipse_areas(major_values, minor_values)
    print(areas)
    single_area = compute_ellipse_area_single(6.0, 4.0)
    print(single_area)