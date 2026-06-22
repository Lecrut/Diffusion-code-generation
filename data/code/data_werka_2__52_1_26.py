import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    @staticmethod
    def calculate_area(radius):
        return Circle.PI * radius ** 2
    
    def get_area(self):
        return Circle.calculate_area(self.radius)

if __name__ == '__main__':
    sample_radius1 = 6.0
    sample_radius2 = 12.3
    circle1 = Circle(sample_radius1)
    circle2 = Circle(sample_radius2)
    
    print(f"Area of circle with radius {sample_radius1}: {circle1.get_area()}")
    print(f"Area of circle with radius {sample_radius2}: {circle2.get_area()}")