import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.PI * (self.radius ** 2)

if __name__ == '__main__':
    sample_radii = [1.5, 3.7, 6.0]
    for r in sample_radii:
        circle = Circle(r)
        print(f"The area of a circle with radius {r} is: {circle.area()}")