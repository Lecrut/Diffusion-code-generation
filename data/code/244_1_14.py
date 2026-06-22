class GeometryCalculator:
    RECTANGLE_WIDTH = 10
    RECTANGLE_HEIGHT = 6
    TRIANGLE_BASE = 8
    TRIANGLE_HEIGHT = 5

    @staticmethod
    def calculate_rectangle_area(width, height):
        return width * height

    @staticmethod
    def calculate_triangle_area(base, height):
        return 0.5 * base * height

    @staticmethod
    def sum_areas():
        rectangle_area = GeometryCalculator.calculate_rectangle_area(
            GeometryCalculator.RECTANGLE_WIDTH, 
            GeometryCalculator.RECTANGLE_HEIGHT
        )
        triangle_area = GeometryCalculator.calculate_triangle_area(
            GeometryCalculator.TRIANGLE_BASE, 
            GeometryCalculator.TRIANGLE_HEIGHT
        )
        return rectangle_area + triangle_area

if __name__ == '__main__':
    result = GeometryCalculator.sum_areas()
    print(result)