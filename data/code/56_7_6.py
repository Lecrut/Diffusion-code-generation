import math

class AreaComparer:
    def __init__(self, radius, side_length):
        self.radius = radius
        self.side_length = side_length
        self.circle_area = self.calculate_circle_area()
        self.square_area = self.calculate_square_area()

    def calculate_circle_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_square_area(self):
        return self.side_length ** 2

    def compare_areas(self):
        if self.circle_area > self.square_area:
            difference = self.circle_area - self.square_area
            larger_figure = "circle"
        elif self.square_area > self.circle_area:
            difference = self.square_area - self.circle_area
            larger_figure = "square"
        else:
            difference = 0.0
            larger_figure = "equal"
        return {
            "circle_area": self.circle_area,
            "square_area": self.square_area,
            "larger_figure": larger_figure,
            "difference": difference
        }

if __name__ == '__main__':
    comparer = AreaComparer(radius=5, side_length=6)
    result = comparer.compare_areas()
    print(result)