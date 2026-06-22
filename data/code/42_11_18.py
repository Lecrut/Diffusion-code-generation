import math

def compute_ellipse_areas(major_axes: list[float], minor_axes: list[float]) -> list[float]:
    if not isinstance(major_axes, list):
        raise TypeError("major_axes must be a list")
    if not isinstance(minor_axes, list):
        raise TypeError("minor_axes must be a list")
    if len(major_axes) != len(minor_axes):
        raise ValueError("major_axes and minor_axes must have the same length")
    
    areas = []
    for a, b in zip(major_axes, minor_axes):
        if not isinstance(a, (int, float)):
            raise TypeError(f"Major axis value {a} is not a number")
        if not isinstance(b, (int, float)):
            raise TypeError(f"Minor axis value {b} is not a number")
        area = math.pi * a * b
        areas.append(area)
    
    return areas

if __name__ == '__main__':
    major_axes = [5.0, 10.0, 1.5]
    minor_axes = [3.0, 4.0, 2.0]
    result = compute_ellipse_areas(major_axes, minor_axes)
    print(result)