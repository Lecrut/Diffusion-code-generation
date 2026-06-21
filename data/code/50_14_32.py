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
    circle1 = Circle(5.0)
    circle2 = Circle(3.0)
    difference = compute_area_difference(circle1, circle2)
    print(difference)

    circle3 = Circle(7.5)
    circle4 = Circle(2.0)
    another_difference = compute_area_difference(circle3, circle4)
    print(another_difference)