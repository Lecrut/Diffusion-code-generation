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
            raise ValueError('Radius must be positive')
        self._radius = value

    def calculate_area(self):
        return math.pi * self.radius ** 2

def validate_input(func):

    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError('All inputs must be positive numbers')
        return func(*args, **kwargs)
    return wrapper

@validate_input
def calculate_circle_area(radius):
    return CircleAreaCalculator(radius).calculate_area()
if __name__ == '__main__':
    try:
        print(calculate_circle_area(5.0))
        print(calculate_circle_area(-3.0))
    except ValueError as e:
        print(e)