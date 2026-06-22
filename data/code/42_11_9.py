import math

def compute_ellipse_areas(axis_pairs: list[tuple[float, float]]) -> list[float]:
    if not isinstance(axis_pairs, list):
        raise TypeError('axis_pairs must be a list')
    areas = []
    for pair in axis_pairs:
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise ValueError('Each pair must be a tuple of two numbers')
        major, minor = pair
        if not isinstance(major, (int, float)) or not isinstance(minor, (int, float)):
            raise TypeError('Axis values must be numbers')
        if major <= 0 or minor <= 0:
            raise ValueError('Axis values must be positive')
        area = math.pi * major * minor
        areas.append(area)
    return areas
if __name__ == '__main__':
    sample_pairs = [(5.0, 3.0), (10.0, 7.5), (2.5, 2.5)]
    results = compute_ellipse_areas(sample_pairs)
    print(results)