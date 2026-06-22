import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def compute_area_difference(circle1, circle2):
    return abs(circle1.area() - circle2.area())

if __name__ == '__main__':
    circle_a = Circle(6.0)
    circle_b = Circle(4.5)
    difference = compute_area_difference(circle_a, circle_b)
    print(f"Area difference between circle with radius {circle_a.radius} and {circle_b.radius}: {difference}")