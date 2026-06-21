import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    @staticmethod
    def calculate_area(radius):
        return Circle.PI * (radius ** 2)

if __name__ == '__main__':
    sample_radii = [4, 9, 12]
    for index, radius in enumerate(sample_radii, start=1):
        try:
            area = Circle.calculate_area(radius)
            print(f"Sample {index}: The area of a circle with radius {radius} is {area:.2f}")
        except ValueError as e:
            print(e)