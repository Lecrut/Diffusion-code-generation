import math

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
    
    def calculate_perimeter(self):
        return self.diameter * math.pi

if __name__ == '__main__':
    sample_diameter = 25
    circle_instance = Circle(sample_diameter)
    perimeter = circle_instance.calculate_perimeter()
    print(perimeter)