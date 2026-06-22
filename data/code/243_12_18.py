import math

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def perimeter(self):
        return self.diameter * math.pi

if __name__ == '__main__':
    sample_diameter = 10
    circle_instance = Circle(sample_diameter)
    print(circle_instance.perimeter)