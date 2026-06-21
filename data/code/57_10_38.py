import math

def compute_circle_area(radius):
    return math.pi * (radius ** 2)

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def area(self):
        return compute_circle_area(self.radius)
    
    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 5
    circle_instance = Circle(sample_radius)
    print("Area:", circle_instance.area())
    print("Circumference:", circle_instance.circumference())