import math

PI_CONSTANT = math.pi

class Circle:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def compute_area(self):
        return PI_CONSTANT * self.radius ** 2

if __name__ == '__main__':
    sample_radius = 7.5
    circle_instance = Circle(sample_radius)
    calculated_area = circle_instance.compute_area()
    print(calculated_area)