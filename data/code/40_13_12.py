import math

def validate_positive_dims(dims):
    if len(dims) != 3:
        raise ValueError("Box must have exactly 3 dimensions")
    for d in dims:
        if not isinstance(d, (int, float)) or d <= 0:
            raise ValueError("Dimensions must be positive numbers")
    return True

def compute_surface_area(dimensions):
    validate_positive_dims(dimensions)
    l, w, h = dimensions
    return 2 * (l * w + l * h + w * h)

class Box:
    def __init__(self, length, width, height):
        self.l = length
        self.w = width
        self.h = height

    def surface_area(self):
        return compute_surface_area([self.l, self.w, self.h])

if __name__ == '__main__':
    box = Box(4, 6, 8)
    print(box.surface_area())