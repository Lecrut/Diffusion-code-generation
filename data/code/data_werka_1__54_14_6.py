import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

def calculate_circle_area(radius):
    return Circle(radius).area()

if __name__ == '__main__':
    circle_config = {
        'radius': 6.0
    }
    try:
        area = calculate_circle_area(circle_config['radius'])
        print(f"Area of the circle with radius {circle_config['radius']}: {area}")
    except ValueError as e:
        print(e)