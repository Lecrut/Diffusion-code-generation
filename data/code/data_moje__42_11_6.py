import math

def compute_ellipse_areas(major_axes, minor_axes):
    if not isinstance(major_axes, list) or not isinstance(minor_axes, list):
        raise TypeError('Both major_axes and minor_axes must be lists.')
    if len(major_axes) != len(minor_axes):
        raise ValueError('major_axes and minor_axes must have the same length.')
    areas = []
    for major, minor in zip(major_axes, minor_axes):
        if not isinstance(major, (int, float)) or not isinstance(minor, (int, float)):
            raise TypeError('Axis values must be numeric (int or float).')
        if major <= 0 or minor <= 0:
            raise ValueError('Axis values must be positive.')
        area = math.pi * major * minor / 4
        areas.append(area)
    return areas
if __name__ == '__main__':
    sample_major_axes = [10, 20, 15, 5]
    sample_minor_axes = [5, 10, 8, 3]
    computed_areas = compute_ellipse_areas(sample_major_axes, sample_minor_axes)
    for i, area in enumerate(computed_areas):
        print(f'Ellipse {i + 1} area: {area}')