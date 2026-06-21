import math

class TriangleCalculator:
    def __init__(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")
        self.height = height
        self.side_length = self.calculate_side_length()
        self.perimeter = self.calculate_perimeter()

    def calculate_side_length(self):
        return (2 * self.height) / math.sqrt(3)

    def calculate_perimeter(self):
        return 3 * self.side_length

if __name__ == '__main__':
    try:
        calculator = TriangleCalculator(height=8.73)
        print(f'Side Length: {calculator.calculate_side_length()}')
        print(f'Perimeter: {calculator.calculate_perimeter()}')
    except ValueError as e:
        print(e)