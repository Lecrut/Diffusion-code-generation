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
    circle_a = Circle(5.0)
    circle_b = Circle(3.0)
    difference = compute_area_difference(circle_a, circle_b)
    print(difference)

    circle_c = Circle(7.5)
    circle_d = Circle(2.0)
    another_difference = compute_area_difference(circle_c, circle_d)
    print(another_difference)