import math
from functools import wraps

def validate_positive_radius(func):
    @wraps(func)
    def wrapper(radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        return func(radius)
    return wrapper

@validate_positive_radius
def calculate_circle_area(radius):
    return math.pi * radius ** 2

class CircleCalculator:
    def __init__(self):
        self._cache = {}

    @validate_positive_radius
    def get_area(self, radius):
        if radius not in self._cache:
            self._cache[radius] = calculate_circle_area(radius)
        return self._cache[radius]

if __name__ == '__main__':
    calculator = CircleCalculator()
    print(calculator.get_area(10))
    print(calculator.get_area(7.5))
    print(calculate_circle_area(3))
    try:
        calculate_circle_area(-5)
    except ValueError as e:
        print(e)
    try:
        calculate_circle_area("string")
    except TypeError as e:
        print(e)