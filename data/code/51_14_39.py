import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius_1 = 4.0
    sample_radius_2 = 9.5
    circle1 = Circle(sample_radius_1)
    circle2 = Circle(sample_radius_2)
    
    print(circle1.perimeter())
    print(circle2.perimeter())