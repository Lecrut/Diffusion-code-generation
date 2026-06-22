import math

def _validate_radius(r):
    if r < 0:
        raise ValueError("Radius must be non-negative")
    return r

def circle_area(r):
    return math.pi * _validate_radius(r) ** 2

if __name__ == '__main__':
    print(circle_area(10))
    print(circle_area(3.5))