import math

class ConeGeometry:
    def __init__(self, radius, height):
        if radius < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        self.radius = radius
        self.height = height

    def volume(self):
        return (1 / 3) * math.pi * (self.radius ** 2) * self.height

    def base_area(self):
        return math.pi * (self.radius ** 2)

    def slant_height(self):
        return math.sqrt(self.radius ** 2 + self.height ** 2)

if __name__ == '__main__':
    r = 7.0
    h = 14.0
    cone = ConeGeometry(r, h)
    print(cone.volume())
    print(cone.base_area())
    print(cone.slant_height())