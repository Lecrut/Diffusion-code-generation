import math

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1 / 3) * math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        slant = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * (self.radius + slant)

if __name__ == '__main__':
    cone = Cone(6, 9)
    print(cone.volume())
    print(cone.surface_area())