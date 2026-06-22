import math

class Geometry:
    def __init__(self):
        self.circle_radius = 5

    def calculate_circle_area(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2

if __name__ == '__main__':
    geometry = Geometry()
    try:
        area = geometry.calculate_circle_area(geometry.circle_radius)
        print(area)
    except ValueError as e:
        print(e)