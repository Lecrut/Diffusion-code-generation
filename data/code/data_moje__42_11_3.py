import math

def compute_ellipse_areas(major_axes, minor_axes):
    if not isinstance(major_axes, list) or not isinstance(minor_axes, list):
        raise TypeError('Inputs must be lists.')
    if len(major_axes) != len(minor_axes):
        raise ValueError('Lists must have the same length.')
    areas = []
    for major, minor in zip(major_axes, minor_axes):
        if not isinstance(major, (int, float)):
            raise TypeError('Major axis must be a numeric type.')
        if not isinstance(minor, (int, float)):
            raise TypeError('Minor axis must be a numeric type.')
        if major <= 0 or minor <= 0:
            raise ValueError('Axes must be positive numbers.')
        area = math.pi * (major / 2) * (minor / 2)
        areas.append(area)
    return areas
if __name__ == '__main__':
    sample_major_axes = [10.0, 5.0, 8.0]
    sample_minor_axes = [6.0, 3.0, 4.0]
    computed_areas = compute_ellipse_areas(sample_major_axes, sample_minor_axes)
    for i, area in enumerate(computed_areas):
        print(f'Ellipse {i + 1} area: {area}')