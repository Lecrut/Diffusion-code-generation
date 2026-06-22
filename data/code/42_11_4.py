import math

def compute_ellipse_areas(major_axes: list[float], minor_axes: list[float]) -> list[float]:
    if len(major_axes) != len(minor_axes):
        raise ValueError("Major and minor axis lists must have the same length.")
    
    areas = []
    for major, minor in zip(major_axes, minor_axes):
        if major < 0 or minor < 0:
            raise ValueError("Axis lengths cannot be negative.")
        area = math.pi * major * minor
        areas.append(area)
    return areas

if __name__ == '__main__':
    majors = [5.0, 10.0, 7.5]
    minores = [3.0, 4.0, 2.5]
    
    result = compute_ellipse_areas(majors, minores)
    
    print(result)