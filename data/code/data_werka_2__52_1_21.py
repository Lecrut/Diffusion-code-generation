import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    sample_radius1 = 6.0
    sample_radius2 = 12.5
    circle1 = Circle(sample_radius1)
    circle2 = Circle(sample_radius2)
    
    print(f"Area of circle with radius {sample_radius1}: {circle1.area()}")
    print(f"Diameter of circle with radius {sample_radius1}: {circle1.diameter()}")
    print(f"Area of circle with radius {sample_radius2}: {circle2.area()}")
    print(f"Diameter of circle with radius {sample_radius2}: {circle2.diameter()}")