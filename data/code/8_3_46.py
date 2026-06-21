import math

class Circle:
    PI = math.pi

    @staticmethod
    def calculate_area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return Circle.PI * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 4.25
    circle = Circle()
    area = circle.calculate_area(sample_radius)
    print(area)