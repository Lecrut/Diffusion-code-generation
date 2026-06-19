import math

class GeometryUtils:
    PI = math.pi

    @staticmethod
    def calculate_area_rectangle(length, width):
        return length * width

    @staticmethod
    def calculate_area_circle(radius):
        return GeometryUtils.PI * radius ** 2

class AreaComparator:
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    def compare(self):
        rectangle_area = GeometryUtils.calculate_area_rectangle(self.length, self.width)
        circle_area = GeometryUtils.calculate_area_circle(self.radius)
        print(f"Rectangle Area: {rectangle_area:.2f}")
        print(f"Circle Area: {circle_area:.2f}")

if __name__ == '__main__':
    length = 8.0
    width = 4.5
    radius = 6.2
    comparator = AreaComparator(length, width, radius)
    comparator.compare()