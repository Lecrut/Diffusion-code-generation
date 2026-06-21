class TriangleCalculator:
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, base):
        if base <= 0:
            raise ValueError("Base must be a positive number.")
        self.base = base

    def set_height(self, height):
        if height <= 0:
            raise ValueError("Height must be a positive number.")
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        calculator = TriangleCalculator()
        calculator.set_base(9)
        calculator.set_height(4)
        print("Area of the triangle:", calculator.calculate_area())
    except ValueError as e:
        print(e)

    try:
        invalid_calculator = TriangleCalculator()
        invalid_calculator.set_base(-2)
        invalid_calculator.set_height(5)
        print("Area of the triangle:", invalid_calculator.calculate_area())
    except ValueError as e:
        print(e)