import math

class Circle:
    RADIUS = 5.0

    @staticmethod
    def calculate_area(radius):
        return math.pi * radius ** 2

if __name__ == '__main__':
    area = Circle.calculate_area(Circle.RADIUS)
    print(area)