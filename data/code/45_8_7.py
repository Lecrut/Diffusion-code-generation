import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def area(self):
        return self._calculate_area()
    
    def _calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        sample_radius = 8
        circle = Circle(sample_radius)
        calculated_area = circle.area()
        print(f"The area of a circle with radius {sample_radius} is: {calculated_area}")
    except ValueError as e:
        print(e)