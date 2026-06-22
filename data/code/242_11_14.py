class Geometry:
    def __init__(self, side_length_square, base_triangle, height_triangle):
        self.side_length_square = side_length_square
        self.base_triangle = base_triangle
        self.height_triangle = height_triangle

    def calculate_area_square(self):
        return self.side_length_square ** 2

    def calculate_area_triangle(self):
        return 0.5 * self.base_triangle * self.height_triangle

    def is_square_area_greater(self):
        area_square = self.calculate_area_square()
        area_triangle = self.calculate_area_triangle()
        return area_square > area_triangle

if __name__ == '__main__':
    geometry = Geometry(5, 4, 6)
    print(geometry.is_square_area_greater())