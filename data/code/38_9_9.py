import math

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1 / 3) * math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        slant_height = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * (self.radius + slant_height)

if __name__ == '__main__':
    cone_instance = Cone(10, 20)
    vol = cone_instance.volume()
    area = cone_instance.surface_area()
    print(vol)
    print(area)