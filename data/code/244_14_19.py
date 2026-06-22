class ShapeCalculator:
    def calculate_circle_area(self, radius):
        return 3.14159 * (radius ** 2)
    
    def calculate_square_area(self, side):
        return side ** 2

if __name__ == '__main__':
    calculator = ShapeCalculator()
    circle_radius = 3
    square_side = 4
    total_area = calculator.calculate_circle_area(circle_radius) + calculator.calculate_square_area(square_side)
    print(total_area)