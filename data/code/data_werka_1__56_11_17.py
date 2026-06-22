import math

class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * (radius ** 2)
    
    def calculate_square_perimeter(self, side):
        return 4 * side
    
    def total_areas_and_perimeters(self, circle_radius1, circle_radius2, square_side1, square_side2):
        total_circle_area = self.calculate_circle_area(circle_radius1) + self.calculate_circle_area(circle_radius2)
        total_square_perimeter = self.calculate_square_perimeter(square_side1) + self.calculate_square_perimeter(square_side2)
        return {
            'total_circle_area': total_circle_area,
            'total_square_perimeter': total_square_perimeter
        }

if __name__ == '__main__':
    calculator = GeometryCalculator()
    
    circle_radius1 = 3.0
    circle_radius2 = 4.5
    square_side1 = 2.0
    square_side2 = 6.0
    
    result = calculator.total_areas_and_perimeters(circle_radius1, circle_radius2, square_side1, square_side2)
    
    print(f"Total Circle Area: {result['total_circle_area']}")
    print(f"Total Square Perimeter: {result['total_square_perimeter']}")