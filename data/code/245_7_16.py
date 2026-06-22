import math

class ShapeComparer:
    def __init__(self, semi_major_axis, semi_minor_axis, side_length):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis
        self.side_length = side_length

    def calculate_ellipse_area(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis

    def calculate_rectangle_area(self):
        return self.side_length ** 2

    def compare_areas(self):
        ellipse_area = self.calculate_ellipse_area()
        rectangle_area = self.calculate_rectangle_area()
        difference = abs(ellipse_area - rectangle_area)
        print(f"Ellipse area: {ellipse_area}")
        print(f"Rectangle area: {rectangle_area}")
        print(f"Difference between areas: {difference}")

if __name__ == '__main__':
    comparer = ShapeComparer(5, 10, 4)
    comparer.compare_areas()