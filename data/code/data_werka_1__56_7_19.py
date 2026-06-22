import math

class AreaComparison:
    PI = math.pi

    @staticmethod
    def calculate_circle_area(radius):
        return AreaComparison.PI * (radius ** 2)

    @staticmethod
    def calculate_square_area(side_length):
        return side_length ** 2

    @staticmethod
    def compare_areas(radius, side_length):
        circle_area = AreaComparison.calculate_circle_area(radius)
        square_area = AreaComparison.calculate_square_area(side_length)
        
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
    side_length = 4
    result = AreaComparison.compare_areas(radius, side_length)
    print(result)