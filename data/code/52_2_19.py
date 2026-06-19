import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_radius1 = 4
    sample_radius2 = 9.5

    try:
        circle1 = Circle(sample_radius1)
        print(f"The area of the circle with radius {sample_radius1} is {circle1.area():.2f}")
        print(f"The circumference of the circle with radius {sample_radius1} is {circle1.circumference():.2f}")
    except ValueError as e:
        print(e)

    try:
        circle2 = Circle(sample_radius2)
        print(f"The area of the circle with radius {sample_radius2} is {circle2.area():.2f}")
        print(f"The circumference of the circle with radius {sample_radius2} is {circle2.circumference():.2f}")
    except ValueError as e:
        print(e)