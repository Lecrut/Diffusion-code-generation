import math

_CONE_COEFFICIENT = math.pi / 3

class ConeGeometry:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def validate(self):
        if self.radius <= 0:
            raise ValueError("Radius must be positive.")
        if self.height <= 0:
            raise ValueError("Height must be positive.")

    def volume(self):
        self.validate()
        return _CONE_COEFFICIENT * (self.radius ** 2) * self.height

def calculate_cone_volume(radius, height):
    cone = ConeGeometry(radius, height)
    return cone.volume()

if __name__ == '__main__':
    r = 4.0
    h = 7.5
    result = calculate_cone_volume(r, h)
    print(result)