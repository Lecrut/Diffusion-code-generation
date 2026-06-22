import math
import functools

@functools.lru_cache(maxsize=None)
def _get_pi():
    return math.pi

def calculate_ellipse_area(semi_major, semi_minor):
    a = float(semi_major)
    b = float(semi_minor)
    if a < 0:
        raise ValueError("Semi-major axis must be non-negative")
    if b < 0:
        raise ValueError("Semi-minor axis must be non-negative")
    if not math.isfinite(a):
        raise OverflowError("Semi-major axis must be finite")
    if not math.isfinite(b):
        raise OverflowError("Semi-minor axis must be finite")
    return _get_pi() * a * b

if __name__ == '__main__':
    semi_major_axis = 5.0
    semi_minor_axis = 3.0
    area = calculate_ellipse_area(semi_major_axis, semi_minor_axis)
    print(area)