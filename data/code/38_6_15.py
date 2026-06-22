import math

def _validate_dimensions(r, h):
    if not isinstance(r, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Dimensions must be numeric")
    if r <= 0 or h <= 0:
        raise ValueError("Dimensions must be positive")
    return True

def cone_volume(radius, height):
    _validate_dimensions(radius, height)
    base_area = math.pi * radius * radius
    return base_area * height / 3.0

class Cone:
    def __init__(self, radius, height):
        _validate_dimensions(radius, height)
        self.radius = radius
        self.height = height

    def volume(self):
        return cone_volume(self.radius, self.height)

if __name__ == '__main__':
    r_val = 1
    h_val = 3
    my_cone = Cone(r_val, h_val)
    print(my_cone.volume())