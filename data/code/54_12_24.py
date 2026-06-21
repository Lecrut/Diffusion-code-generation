import math

class Circle:
    PI = 3.141592653589793
    
    @staticmethod
    def validate_radius(radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
    
    def __init__(self, radius: float):
        Circle.validate_radius(radius)
        self.radius = radius
    
    def calculate_area(self) -> float:
        return Circle.PI * self.radius ** 2

if __name__ == '__main__':
    circle1 = Circle(5.0)
    area1 = circle1.calculate_area()
    print(f"Area of circle with radius 5.0: {area1}")