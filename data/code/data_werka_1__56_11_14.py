import math

class AreaPerimeterCalculator:
    def __init__(self):
        self.circle_area = 0
        self.circle_perimeter = 0
        self.square_perimeter = 0

    def validate_radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
    
    def validate_side_length(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")

    def calculate_circles_area(self, radii):
        total_area = 0
        for radius in radii:
            self.validate_radius(radius)
            total_area += math.pi * (radius ** 2)
        return total_area

    def calculate_squares_perimeter(self, side_lengths):
        total_perimeter = 0
        for side_length in side_lengths:
            self.validate_side_length(side_length)
            total_perimeter += 4 * side_length
        return total_perimeter

def main():
    calculator = AreaPerimeterCalculator()
    circle_radii = [3.0, 4.5]
    square_sides = [2.0, 6.0]

    circles_area = calculator.calculate_circles_area(circle_radii)
    squares_perimeter = calculator.calculate_squares_perimeter(square_sides)

    result = {
        "total_circle_area": circles_area,
        "total_square_perimeter": squares_perimeter
    }

    print(result)

if __name__ == '__main__':
    main()