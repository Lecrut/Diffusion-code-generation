import math

def compute_ellipse_area(major_axis, minor_axis):
    if major_axis <= 0 or minor_axis <= 0:
        raise ValueError('Both major and minor axes must be positive numbers.')
    return math.pi * major_axis * minor_axis / 4

def compute_ellipse_areas(major_axes, minor_axes):
    if len(major_axes) != len(minor_axes):
        raise ValueError('major_axes and minor_axes must have the same length.')
    areas = []
    for major, minor in zip(major_axes, minor_axes):
        areas.append(compute_ellipse_area(major, minor))
    return areas
if __name__ == '__main__':
    major_axes = [10.0, 5.0, 12.5, 7.8]
    minor_axes = [6.0, 3.0, 4.2, 2.1]
    areas = compute_ellipse_areas(major_axes, minor_axes)
    for area in areas:
        print(area)