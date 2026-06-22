import math

class Circle:
    PI = math.pi
    
    def __init__(self, diameter):
        if diameter <= 0:
            raise ValueError("Diameter must be positive")
        self.diameter = diameter
    
    @staticmethod
    def calculate_area(diameter):
        if diameter <= 0:
            raise ValueError("Diameter must be positive")
        radius = diameter / 2
        return Circle.PI * (radius ** 2)
    
    def area(self):
        return Circle.calculate_area(self.diameter)

if __name__ == '__main__':
    sample_diameters = [7, 15, -2, 0]
    for diameter in sample_diameters:
        try:
            circle = Circle(diameter)
            print(f"Area of circle with diameter {diameter}: {circle.area()}")
        except ValueError as e:
            print(f"Error for diameter {diameter}: {e}")