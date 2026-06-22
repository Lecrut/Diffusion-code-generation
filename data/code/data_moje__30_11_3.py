import math

class CircleMetrics:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    radius_value = 5
    circle_obj = CircleMetrics(radius_value)
    print(circle_obj.area())