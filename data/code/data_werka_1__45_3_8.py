import math

class Circle:
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

    def area(self):
        return math.pi * (self.radius ** 2)

def validate_radius(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, Circle) and arg.radius <= 0:
                raise ValueError("Radius must be positive")
            elif not isinstance(arg, Circle) and arg <= 0:
                raise ValueError("Radius must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_radius
def print_circle_area(circle):
    print(f"The area of the circle is: {circle.area()}")

if __name__ == '__main__':
    try:
        circle1 = Circle(5.0)
        circle2 = Circle(7.5)

        print_circle_area(circle1)
        print_circle_area(circle2)
    except ValueError as e:
        print(e)