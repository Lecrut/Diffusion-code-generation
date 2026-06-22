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

def area_decorator(func):
    def wrapper(radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        return func(radius)
    return wrapper

@area_decorator
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    try:
        circle = CircleAreaCalculator(7.5)
        print(circle.calculate_area())
        
        radius_value = 10.0
        area_value = calculate_circle_area(radius_value)
        print(area_value)
    except ValueError as e:
        print(e)