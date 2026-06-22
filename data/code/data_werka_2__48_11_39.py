class SquareCalculator:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def calculate_side_length(self):
        return self.area ** 0.5

    def calculate_perimeter(self):
        side_length = self.calculate_side_length()
        return 4 * side_length

if __name__ == '__main__':
    try:
        square_area = 16
        calculator = SquareCalculator(square_area)
        side_length = calculator.calculate_side_length()
        perimeter = calculator.calculate_perimeter()
        print(f"Side Length: {side_length}, Perimeter: {perimeter}")
    except ValueError as e:
        print(e)