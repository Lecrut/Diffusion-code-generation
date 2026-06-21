import math

def _validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return True

def compute_area(radius):
    _validate_radius(radius)
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    r = 5
    area_result = compute_area(r)
    print(area_result)