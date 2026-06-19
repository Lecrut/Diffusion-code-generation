import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    hard_coded_radius = 4.5
    circle_instance = Circle(hard_coded_radius)
    perimeter = circle_instance.calculate_perimeter()
    print(perimeter)