import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    SAMPLE_RADIUS_1 = 3.0
    SAMPLE_RADIUS_2 = 4.5
    SAMPLE_RADIUS_3 = 7.0

    circle1 = Circle(SAMPLE_RADIUS_1)
    circle2 = Circle(SAMPLE_RADIUS_2)
    circle3 = Circle(SAMPLE_RADIUS_3)

    print(f"The area of circle with radius {SAMPLE_RADIUS_1} is: {circle1.area()}")
    print(f"The area of circle with radius {SAMPLE_RADIUS_2} is: {circle2.area()}")
    print(f"The area of circle with radius {SAMPLE_RADIUS_3} is: {circle3.area()}")