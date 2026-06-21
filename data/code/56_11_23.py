import math

class GeometryCalculator:
    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def calculate_square_perimeter(side_length):
        return 4 * side_length

def calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2):
    total_circle_area = GeometryCalculator.calculate_circle_area(circle_radius1) + GeometryCalculator.calculate_circle_area(circle_radius2)
    total_square_perimeter = GeometryCalculator.calculate_square_perimeter(square_side1) + GeometryCalculator.calculate_square_perimeter(square_side2)
    return {'total_circle_area': total_circle_area, 'total_square_perimeter': total_square_perimeter}

if __name__ == '__main__':
    circle_radius1 = 5
    circle_radius2 = 8
    square_side1 = 3
    square_side2 = 7
    result = calculate_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2)
    print(result)