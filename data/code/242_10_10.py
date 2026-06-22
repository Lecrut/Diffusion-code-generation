import math

class ShapeAreaComparer:
    def __init__(self, circle_radius, rectangle_length, rectangle_width):
        self.circle_radius = circle_radius
        self.rectangle_length = rectangle_length
        self.rectangle_width = rectangle_width

    def calculate_circle_area(self):
        return math.pi * self.circle_radius ** 2

    def calculate_rectangle_area(self):
        return self.rectangle_length * self.rectangle_width

    def compare_areas(self):
        circle_area = self.calculate_circle_area()
        rectangle_area = self.calculate_rectangle_area()

        if circle_area > rectangle_area:
            print(f"The circle with radius {self.circle_radius} has a larger area: {circle_area}")
        elif circle_area < rectangle_area:
            print(f"The rectangle with dimensions {self.rectangle_length}x{self.rectangle_width} has a larger area: {rectangle_area}")
        else:
            print("Both shapes have the same area.")

if __name__ == '__main__':
    comparer = ShapeAreaComparer(5, 10, 7)
    comparer.compare_areas()