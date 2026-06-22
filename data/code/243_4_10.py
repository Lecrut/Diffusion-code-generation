import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 5.0
    circle_instance = Circle(sample_radius)
    perimeter = circle_instance.calculate_perimeter()
    print(perimeter)