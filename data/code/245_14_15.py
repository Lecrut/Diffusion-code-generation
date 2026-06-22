import math

class GeometryComparison:
    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * radius**2
    
    @staticmethod
    def calculate_square_area(side):
        return side * side
    
    @staticmethod
    def compare_areas(circle_radius, square_side):
        circle_area = GeometryComparison.calculate_circle_area(circle_radius)
        square_area = GeometryComparison.calculate_square_area(square_side)
        if math.isclose(circle_area, square_area, rel_tol=1e-9):
            return "The areas are equal."
        else:
            difference = abs(circle_area - square_area)
            return f"The areas are not equal. Difference: {difference}"

if __name__ == '__main__':
    circle_radius = 5.0
    square_side = 5.0
    result = GeometryComparison.compare_areas(circle_radius, square_side)
    print(result)