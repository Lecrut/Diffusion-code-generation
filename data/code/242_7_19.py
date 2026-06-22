class ShapeAreaCalculator:
    @staticmethod
    def area_rhombus(d1, d2):
        return 0.5 * d1 * d2

    @staticmethod
    def area_square(side):
        return side ** 2

if __name__ == '__main__':
    calculator = ShapeAreaCalculator()
    rhombus_area = calculator.area_rhombus(10, 8)
    square_area = calculator.area_square(6)
    print(f"Rhombus Area: {rhombus_area}")
    print(f"Square Area: {square_area}")