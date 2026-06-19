import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_values = [1, 2, 0, 10, 5.5]
    for value in sample_values:
        try:
            circle = Circle(value)
            print(f"Area of circle with radius {value}: {circle.area()}")
        except ValueError as e:
            print(e)