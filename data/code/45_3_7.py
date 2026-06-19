import math

class CircleAreaCalculator:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

def validate_radius(func):
    def wrapper(radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        return func(radius)
    return wrapper

@validate_radius
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    try:
        circle = CircleAreaCalculator(5.0)
        print(circle.calculate_area())
        
        print(calculate_circle_area(3.0))
    except (ValueError, TypeError) as e:
        print(e)