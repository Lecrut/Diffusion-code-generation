import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius = 5.0
    circle_instance = Circle(sample_radius)
    
    print(f"Radius: {sample_radius}")
    print(f"Circumference: {circle_instance.calculate_perimeter()}")