import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    try:
        circle1 = Circle(radius=3)
        print(circle1.perimeter())
        print(circle1.diameter())
        
        circle2 = Circle(radius=8.5)
        print(circle2.perimeter())
        print(circle2.diameter())
    except ValueError as e:
        print(e)