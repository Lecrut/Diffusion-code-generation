import math

class Circle:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError("Radius must be a non-negative number")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def calculate_circle_area(radius):
    circle = Circle(radius)
    return circle.area()

if __name__ == '__main__':
    try:
        sample_radius = 3.0
        area_result = calculate_circle_area(sample_radius)
        print(f"The area of the circle with radius {sample_radius} is: {area_result}")
    except ValueError as e:
        print(e)