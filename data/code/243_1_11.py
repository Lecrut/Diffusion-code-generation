import math

class Circle:
    RADIUS = 5.0

    @staticmethod
    def calculate_circumference(radius):
        return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = Circle.RADIUS
    circumference = Circle.calculate_circumference(sample_radius)
    print(circumference)