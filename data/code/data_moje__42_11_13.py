import math
import typing

def compute_ellipse_areas(axes_pairs: typing.List[typing.Tuple[float, float]]) -> typing.List[float]:
    if not isinstance(axes_pairs, list):
        raise TypeError('Input must be a list of tuples.')
    results = []
    for pair in axes_pairs:
        if not isinstance(pair, (tuple, list)) or len(pair) != 2:
            raise TypeError('Each element must be a tuple or list with two values.')
        major_axis, minor_axis = pair
        if not isinstance(major_axis, (int, float)):
            raise TypeError(f'Major axis must be a number, got {type(major_axis)}')
        if not isinstance(minor_axis, (int, float)):
            raise TypeError(f'Minor axis must be a number, got {type(minor_axis)}')
        if isinstance(major_axis, bool) or isinstance(minor_axis, bool):
            raise TypeError('Axis values must not be booleans.')
        if major_axis <= 0 or minor_axis <= 0:
            raise ValueError('Axis lengths must be positive.')
        area = math.pi * (major_axis / 2.0) * (minor_axis / 2.0)
        results.append(area)
    return results
if __name__ == '__main__':
    sample_axes_pairs = [(10.0, 5.0), (20.0, 15.0), (7.5, 3.2), (100.0, 100.0), (1.0, 1.0)]
    areas = compute_ellipse_areas(sample_axes_pairs)
    for i, area in enumerate(areas):
        print(areas[i])