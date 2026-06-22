import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius = 5.0
    circle_instance = Circle(sample_radius)
    circumference_result = circle_instance.calculate_circumference()
    print(circumference_result)