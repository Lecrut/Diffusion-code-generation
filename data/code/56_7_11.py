import math

class AreaComparator:
    def __init__(self, radius, side_length):
        if radius < 0 or side_length < 0:
            raise ValueError("Radius and side length must be non-negative.")
        self.radius = radius
        self.side_length = side_length

    def calculate_circle_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_square_area(self):
        return self.side_length ** 2

    def compare_areas(self):
        circle_area = self.calculate_circle_area()
        square_area = self.calculate_square_area()

        if circle_area > square_area:
            larger_figure = "circle"
            difference = circle_area - square_area
        elif square_area > circle_area:
            larger_figure = "square"
            difference = square_area - circle_area
        else:
            larger_figure = "equal"
            difference = 0.0

        return {
            "circle_area": circle_area,
            "square_area": square_area,
            "larger_figure": larger_figure,
            "difference": difference
        }

if __name__ == '__main__':
    radius = 7
    side_length = 10
    comparator = AreaComparator(radius, side_length)
    result = comparator.compare_areas()
    print(result)