import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_values = [1.5, 3.8, 7.2]
    for radius in sample_values:
        try:
            circle = Circle(radius)
            print(f"The area of a circle with radius {radius} is: {circle.area()}")
        except ValueError as e:
            print(e)