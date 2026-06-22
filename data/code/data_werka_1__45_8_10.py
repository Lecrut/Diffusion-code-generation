import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def area(self):
        return self._calculate_area()
    
    def _calculate_area(self):
        return Circle.PI * (self.radius ** 2)

if __name__ == '__main__':
    try:
        circle = Circle(8)
        print(f"Area of the circle with radius 8 is: {circle.area()}")
    except ValueError as e:
        print(e)