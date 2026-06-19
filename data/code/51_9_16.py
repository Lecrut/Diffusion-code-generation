class PerimeterCalculator:

    def __init__(self, sides):
        self.sides = sides

    def validate_sides(self):
        if not all((isinstance(side, (int, float)) for side in self.sides)):
            raise ValueError('All sides must be numeric')
        if any((side < 0 for side in self.sides)):
            raise ValueError('All sides must be non-negative')

    def calculate_perimeter(self):
        self.validate_sides()
        return sum(self.sides)
if __name__ == '__main__':
    try:
        calculator = PerimeterCalculator([3, 4, 5])
        print(calculator.calculate_perimeter())
        calculator = PerimeterCalculator([7.5, 9.2])
        print(calculator.calculate_perimeter())
        calculator = PerimeterCalculator([0, 0, 0])
        print(calculator.calculate_perimeter())
        calculator = PerimeterCalculator([-3, 4, 5])
        print(calculator.calculate_perimeter())
    except ValueError as e:
        print(e)