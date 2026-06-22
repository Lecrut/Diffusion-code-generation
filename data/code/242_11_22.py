class Geometry:
    def __init__(self, side_length_square, base_triangle, height_triangle):
        self.side_length_square = side_length_square
        self.base_triangle = base_triangle
        self.height_triangle = height_triangle

    def calculate_square_area(self):
        return self.side_length_square ** 2

    def calculate_triangle_area(self):
        return 0.5 * self.base_triangle * self.height_triangle

    def compare_areas(self):
        square_area = self.calculate_square_area()
        triangle_area = self.calculate_triangle_area()
        return square_area > triangle_area

if __name__ == '__main__':
    geometry = Geometry(5, 4, 6)
    print(geometry.compare_areas())