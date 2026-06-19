import math

class Circle:
    def __init__(self, radius):
        self.radius = self._validate_radius(radius)
    
    def _validate_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return radius
    
    def area(self):
        return self._calculate_area()
    
    def _calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle = Circle(3)
        print(circle.area())
    except (TypeError, ValueError) as e:
        print(e)