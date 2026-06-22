import math

def calculate_ellipse_areas(axes: list[tuple[float, float]]) -> list[float]:
    if not isinstance(axes, list):
        raise TypeError("axes must be a list")
    areas = []
    for axis in axes:
        if not isinstance(axis, (list, tuple)) or len(axis) != 2:
            raise TypeError("Each axis pair must be a tuple or list of length 2")
        major, minor = axis
        if not isinstance(major, (int, float)) or not isinstance(minor, (int, float)):
            raise TypeError("Axis values must be numeric")
        if major < 0 or minor < 0:
            raise ValueError("Axis values must be non-negative")
        area = math.pi * major * minor
        areas.append(area)
    return areas

if __name__ == '__main__':
    sample_axes = [(5.0, 3.0), (10.0, 2.0), (1.0, 1.0)]
    result = calculate_ellipse_areas(sample_axes)
    for area in result:
        print(area)