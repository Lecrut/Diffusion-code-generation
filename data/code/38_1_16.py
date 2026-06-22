import math

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_volume(self):
        base_area = math.pi * self.radius ** 2
        volume = base_area * self.height / 3
        return volume

if __name__ == '__main__':
    radius_value = 5
    height_value = 10
    cone_instance = Cone(radius_value, height_value)
    print(cone_instance.get_volume())