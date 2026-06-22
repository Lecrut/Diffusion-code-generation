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
    
if __name__ == '__main__':
    sample_radius1 = 6.0
    sample_radius2 = 12.5
    area1 = Circle.calculate_area(sample_radius1)
    area2 = Circle.calculate_area(sample_radius2)
    
    print(f"Area of circle with radius {sample_radius1}: {area1}")
    print(f"Area of circle with radius {sample_radius2}: {area2}")