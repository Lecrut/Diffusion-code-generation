import math

class Circle:
    DEFAULT_RADIUS = 5

    @staticmethod
    def calculate_area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2

if __name__ == '__main__':
    try:
        area = Circle.calculate_area(Circle.DEFAULT_RADIUS)
        print(area)
    except ValueError as e:
        print(e)