import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_circle = Circle(5.0)
    perimeter_result = sample_circle.calculate_perimeter()
    print(perimeter_result)