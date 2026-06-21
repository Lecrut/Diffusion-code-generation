import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        sample_radius = 3.5
        circle_instance = Circle(sample_radius)
        calculated_area = circle_instance.area()
        print(f"The area of the circle with radius {sample_radius} is {calculated_area:.2f}")
    except ValueError as e:
        print(e)