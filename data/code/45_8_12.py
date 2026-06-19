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
        circle1 = Circle(3)
        print("Area of circle with radius 3:", circle1.area())
        
        circle2 = Circle(8)
        print("Area of circle with radius 8:", circle2.area())
        
    except ValueError as e:
        print(e)