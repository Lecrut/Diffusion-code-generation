import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle_radius_1 = 5.0
    circle1 = Circle(circle_radius_1)
    area_of_circle_1 = circle1.calculate_area()
    print(f"Area of circle with radius {circle_radius_1}: {area_of_circle_1}")

    circle_radius_2 = 7.2
    circle2 = Circle(circle_radius_2)
    area_of_circle_2 = circle2.calculate_area()
    print(f"Area of circle with radius {circle_radius_2}: {area_of_circle_2}")