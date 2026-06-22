import math

class Circle:
    RADIUS = 3.5

    @staticmethod
    def calculate_area(radius):
        return math.pi * (radius ** 2)

if __name__ == '__main__':
    radius_value = Circle.RADIUS
    area = Circle.calculate_area(radius_value)
    print(f"The area of the circle with radius {radius_value} is {area:.2f}")