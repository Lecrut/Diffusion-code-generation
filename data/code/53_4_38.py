class SquareCalculator:
    def __init__(self):
        self.results = []

    def calculate_area(self, side):
        if side <= 0:
            raise ValueError("Side length must be positive")
        area = side * side
        self.results.append(area)
        return area

if __name__ == '__main__':
    calculator = SquareCalculator()
    sample_sides = [2, 4, 6, 8]
    for side in sample_sides:
        try:
            print(f"The area of the square with side {side} is: {calculator.calculate_area(side)}")
        except ValueError as e:
            print(e)