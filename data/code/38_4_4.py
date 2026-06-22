import math

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_volume(self):
        return (1/3) * math.pi * self.radius**2 * self.height

    def get_surface_area(self):
        slant_height = math.sqrt(self.radius**2 + self.height**2)
        return math.pi * self.radius * (self.radius + slant_height)

if __name__ == '__main__':
    radius_value = 6
    height_value = 9
    cone_instance = Cone(radius_value, height_value)
    print(cone_instance.get_volume())
    print(cone_instance.get_surface_area())