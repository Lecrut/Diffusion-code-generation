import math
PI = math.pi

class CircleAreaCalculator:

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value

    def calculate_area(self):
        return PI * self.radius ** 2

def area_context_manager(radius):
    if radius <= 0:
        raise ValueError('Radius must be positive')
    yield
if __name__ == '__main__':
    try:
        with area_context_manager(5.0):
            circle = CircleAreaCalculator(5.0)
            print(circle.calculate_area())
    except ValueError as e:
        print(e)
    try:
        with area_context_manager(-3.0):
            circle = CircleAreaCalculator(-3.0)
            print(circle.calculate_area())
    except ValueError as e:
        print(e)